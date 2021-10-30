import cv2
import pyautogui
import numpy as np
import time

SCREEN_SIZE = pyautogui.size()
FPS = 60

codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", codec, FPS, SCREEN_SIZE)

while True:
    img = pyautogui.screenshot()

    frame = np.array(img)

    out.write(frame)

    cv2.imshow('Live', frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
out.release()