from Recorder import Recorder
import numpy as np
import cv2
# pip install opencv-python
# sudo apt-get install scrot
# pip install Pillow
import pyautogui

class ScreenShot(Recorder):
    def __init__(self):
        self.ip = super().get_ip()
        self.mac = super().get_mac()
        self.timestamp = None


    def take_screen_shot(self):
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        cv2.imwrite("image1.png", image)


if __name__ == "__main__":
    # image = pyautogui.screenshot()
    #
    # image = cv2.cvtColor(np.array(image),
    #                      cv2.COLOR_RGB2BGR)
    # cv2.imwrite("image1.png", image)

    screen_shot = ScreenShot()
    screen_shot.take_screen_shot()