from ..models.Screenshot import Screenshot
from .ScreenshotDAO import ScreemshotDAO
from threading import Thread
import os
import uuid
import mss
import mss.tools
import base64
from bson.binary import Binary
from ..Recorder.Recorder import Recorder
import datetime

r = Recorder()



class CaptureScreenshot(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.sdao = ScreemshotDAO()

    def run(self):

        current_dir = os.path.dirname(os.path.abspath(__file__))
        with mss.mss() as sct:
            id = str(uuid.uuid4())

            imagedir = os.path.join(current_dir, f"../temps/{id}.png")
            filename = sct.shot(output=imagedir)
            imgSize = self.get_file_size_in_bytes(filename)

            with open(filename, 'rb') as f:
                img = base64.b64encode(f.read())
                img = img.decode('utf-8')

            os.remove(filename)

            s = Screenshot(r.get_timestamp(), r.get_ip(),
                           r.get_mac(), [], [], img, imgSize, "png")
            self.sdao.create(s)

    def get_file_size_in_bytes(self, file_path):
        size = os.path.getsize(file_path)
        return size
