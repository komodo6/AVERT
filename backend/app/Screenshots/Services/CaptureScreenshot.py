
from ...models.Screenshot import Screenshot
from ..ScreenshotDAO import ScreemshotDAO
from threading import Thread
import os
import uuid
import mss
import mss.tools
import base64
import datetime
from ...models.Annotation import Annotation
from ...Recorder.Recorder import Recorder

r = Recorder()



class CaptureScreenshot(Thread):
    def __init__(self):
        
        Thread.__init__(self)
        self.sdao = ScreemshotDAO()
        self.ip = r.get_ip()
        self.mac = r.get_mac()


    def run(self):
        
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        with mss.mss() as sct:
            id = str(uuid.uuid4())
            imagedir = os.path.join(current_dir, f"../../images/{id}.png")
            filename = sct.shot(output=imagedir)
            a = Annotation(self.ip, None)
            s = Screenshot(r.get_timestamp(
            ), self.ip, self.mac, a.toJSON(), id)
            self.sdao.create(s)

            
            
        # with open(filename, "rb") as img_file:
        #     image64 = base64.b64encode(img_file.read())

        
        
        
            





    