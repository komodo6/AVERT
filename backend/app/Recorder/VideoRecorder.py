import cv2
import pyautogui
import numpy as np
import time

SCREEN_SIZE = pyautogui.size()

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

fps = 120
prev = 0

while True:
    time_elapsed = time.time() - prev

    img = pyautogui.screenshot()q

    if time_elapsed > 1.0/fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
out.release()