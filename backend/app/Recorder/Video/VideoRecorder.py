import cv2
import pyautogui
import numpy as np
import pymongo
import gridfs

client = pymongo.MongoClient(host="54.215.46.201", port=27017)
db = client.AVERT
testCollection = db['myImageCollection']

fs = gridfs.GridFS(db)

SCREEN_SIZE = pyautogui.size()
FPS = 15

codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", codec, FPS, SCREEN_SIZE)

while True:
    img = pyautogui.screenshot()

    frame = np.array(img)

    #to turn it into the right colors, but it was complaining, will fix later
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    out.write(frame)

    #cv2.imshow('Live', frame)

    if cv2.waitKey(1) == ord("q"):
        break

out.release
cv2.destroyAllWindows()

#turning into a string, but not really sure if that works for videos
videoString = out.tostring()

# store the image
imageID = fs.put(videoString, encoding='utf-8')


# create our image meta data
meta = {
    'name': 'myTestSet',
    'video': [
        {
            'videoID': videoID,
            'shape': out.shape,
            'dtype': str(out.dtype)
        }
    ]
}

# insert the meta data
testCollection.insert_one(meta)
