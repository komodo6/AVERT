from ..models.Video import Video
from .VideoDAO import VideoDAO
from threading import Thread
import os
import uuid
from ..Recorder.Recorder import Recorder

r = Recorder()


# define dimensions of screen w.r.t to given monitor to be captured
options = {"top": 40, "left": 100, "width": 100, "height": 100}

# define suitable (Codec,CRF,preset) FFmpeg parameters for writer
output_params = {"-vcodec": "libx264", "-crf": 0, "-preset": "fast"}

# open video stream with defined parameters
stream = ScreenGear(monitor=1, logging=True, **options).start()

# Define writer with defined parameters and suitable output filename for e.g. Output.mp4




class VideoCapture(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.vdao = VideoDAO()
        self.capture = False

    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        id = str(uuid.uuid4())
        writer = WriteGear(output_filename=f"./videos/{id}.mp4", logging=True, **output_params)
        # loop over
        while True:

            # read frames from stream
            frame = stream.read()

            # check for frame if Nonetype
            if self.capture:
                break

            # {do something with the frame here}
            # lets convert frame to gray for this example
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # write gray frame to writer
            writer.write(gray)

            # Show output window
            cv2.imshow("Output Gray Frame", gray)

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
                        r.get_mac(), [], [], resolution="idk", frameRate="id", filename=f"{id}.mp4")
        self.vdao.create(s)

    def stop(self):
        self.capture = True

    def get_file_size_in_bytes(self, file_path):
        size = os.path.getsize(file_path)
        return size
