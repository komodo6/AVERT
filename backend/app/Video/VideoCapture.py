from ..models.Video import Video
from .VideoDAO import VideoDAO
from threading import Thread
import os
import uuid
from vidgear.gears import ScreenGear
from vidgear.gears import WriteGear
import cv2
from ..Recorder.Recorder import Recorder

r = Recorder()


# define dimensions of screen w.r.t to given monitor to be captured
options = {}

# define suitable (Codec,CRF,preset) FFmpeg parameters for writer
output_params = {"-vcodec": "libx264", "-crf": 0, "-preset": "fast"}
# open video stream with defined parameters
stream = ScreenGear(monitor=1, logging=False, **options).start()

# Define writer with defined parameters and suitable output filename for e.g. Output.mp4




class VideoCapture(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.vdao = VideoDAO()
        self.capture = False

    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        #output_params = {"-fourcc":"MJPG"}
        
        id = str(uuid.uuid4())
        writer = WriteGear(output_filename=f"{id}.mp4", compression_mode=True, custom_ffmpeg='', logging=False, **output_params)
        #writer = __init__(self, output_filename='', compression_mode=True, custom_ffmpeg='', logging=False, **output_params)
        # loop over
        while True:

            # read frames from stream
            frame = stream.read()

            # check for frame if Nonetype
            if self.capture:
                break

            # {do something with the frame here}
            # lets convert frame to gray for this example
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # write gray frame to writer
            writer.write(frame)

            # Show output window
            #cv2.imshow("Output Gray Frame", frame)

            # check for 'q' key if pressed
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        # close output window
        cv2.destroyAllWindows()

        # safely close video stream
        stream.stop()

        # safely close writer
        writer.close()



     # TODO: fix attributes
        s = Video(r.get_timestamp(), r.get_ip(),
                        r.get_mac(), [], [], resolution="1080p", frameRate="30", filename=f"{id}.mp4")
        self.vdao.create(s)

    def stop(self):
        self.capture = True
    
    def start(self):
        self.capture = True

    def get_file_size_in_bytes(self, file_path):
        size = os.path.getsize(file_path)
        return size
