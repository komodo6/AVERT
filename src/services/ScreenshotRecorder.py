from Recorder import Recorder
import cv2
# pip install opencv-python
# sudo apt-get install scrot
# pip install Pillow
import pyautogui
from db.db import db
import io
from PIL import Image

class ScreenShotRecorder(Recorder):
    def __init__(self):
        self.ip = super().get_ip()
        self.mac = super().get_mac()
        self.timestamp = None


    def take_screen_shot(self):
        image = pyautogui.screenshot()
        image = image.convert()
        image = image.convert()
        image.show()
        # TODO: make this used as export below
        # image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        # cv2.imwrite("image1.png", image)


        # fs = gridfs.GridFS(db, collection='ScreenShots')
        # fs.put(image)



if __name__ == "__main__":

    # Getting the screen shot
    image = pyautogui.screenshot()
    # image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    # cv2.imwrite("image1.png", image)

    # change the screenshot to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image = {
        'data': image_bytes.getvalue()
    }
    # putting the screen shot into the database
    image_id = db.ScreenShots.insert_one(image).inserted_id

    # geting the current image from the database
    image = db.ScreenShots.find_one({"_id":image_id})
    image = Image.open(io.BytesIO(image['data']))

    # saving that file into the folder
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    cv2.imwrite(str(image_id) + ".png", image)

    # screen_shot = ScreenShot()
    # screen_shot.take_screen_shot()

