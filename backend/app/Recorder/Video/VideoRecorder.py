import cv2
import pyautogui
import numpy as np
import time
from threading import Thread
from pymongo import MongoClient
import gridfs

client = MongoClient('localhost', 27017)
db = client['testDatabaseONE']
testCollection = db['myVideoCollection']

fs = gridfs.GridFS(db)

SCREEN_SIZE = pyautogui.size()
FPS = 10

codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("./output.avi", codec, FPS, SCREEN_SIZE)

while True:
    img = pyautogui.screenshot()

    frame = np.array(img)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    out.write(frame)

    #cv2.imshow('Live', frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
out.release()

videoString = frame.tostring()
videoID = fs.put(videoString, encoding='utf-8')

meta = {
    'name': 'myTestSet',
    'videos': [
        {
            'imageID': videoID,
            'shape': frame.shape,
            'dtype': str(frame.dtype)
        }
    ]
}

testCollection.insert_one(meta)
