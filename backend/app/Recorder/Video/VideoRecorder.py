import cv2
import pyautogui
import numpy as np
import pymongo
import gridfs
import uuid

# X and Y coordinates of mouse pointer
Xs = [0,8,6,14,12,4,2,0]
Ys = [0,2,4,12,14,6,8,0]

client = pymongo.MongoClient(host="54.215.46.201", port=27017)
db = client.AVERT
testCollection = db['myImageCollection']

fs = gridfs.GridFS(db)

SCREEN_SIZE = pyautogui.size()
FPS = 5

videoname = uuid.uuid1()
videoNameString = str(videoname)

codec = cv2.VideoWriter_fourcc(*"XVID")
#
out = cv2.VideoWriter("./Videos/" + videoNameString + ".avi", codec, FPS, SCREEN_SIZE)
# X and Y coordinates of mouse pointer
Xs = [0,8,6,14,12,4,2,0]
Ys = [0,2,4,12,14,6,8,0]

while True:
    img = pyautogui.screenshot()
    mouseX,mouseY = pyautogui.position()
    mouseX *= 2
    mouseY *= 2

    frame = np.array(img)

    #to turn it into the right colors, but it was complaining, will fix later
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Synthesize mouse pointer
    Xthis = [2*x+mouseX for x in Xs]
    Ythis = [2*y+mouseY for y in Ys]
    points = list(zip(Xthis,Ythis))
    points = np.array(points, 'int32')
    cv2.fillPoly(frame,[points],color=[255,255,255])

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
