from ...models.Screenshot import Screenshot
from ..ScreenshotDAO import ScreemshotDAO
from threading import Thread
import os
import uuid
import mss
import mss.tools
import base64


photoID = None

class CaptureScreenshot(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.sdao = ScreemshotDAO()


    def run(self):
        global photoID
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        with mss.mss() as sct:
            id = str(uuid.uuid4())
            photoID = id
            imagedir = os.path.join(current_dir, f"../../images/{id}.png")
            filename = sct.shot(output=imagedir)
            s = Screenshot(None, None, None, None, None, filename, id)
            self.sdao.create(s)

            
            
        with open(filename, "rb") as img_file:
            image64 = base64.b64encode(img_file.read())

        
        
        
            

    def getImage(self):
        return self.image64




    