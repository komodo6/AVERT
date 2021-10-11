from Recorder import Recorder
from models.Screenshot import Screenshot
from db.ScreenshotsDAO import ScreenshotsDOA
from models.Annotation import Annotation
import pyautogui

class ScreenShotRecorder(Recorder):
    def __init__(self):
        self.ip = super().get_ip()
        self.mac = super().get_mac()


    def take_screen_shot(self):
        a = Annotation(self.ip, None)
        image = pyautogui.screenshot()
        screenshot = Screenshot(timestamp=super().get_timestamp(),
                                ip_address=self.ip,
                                mac_address=self.mac,
                                annotations=a.toJSON(),
                                image=image)
        screenshot.save()





