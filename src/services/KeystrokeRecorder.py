from services.Recorder import Recorder
from db.KeystrokeDAO import KeystrokeDAO
from pynput import keyboard
from models.Keystroke import Keystroke
from models.Annotation import Annotation


class KeystrokeRecorder(Recorder):
    def __init__(self) -> None:
        super().__init__()
        self.ip = super().get_ip()
        self.mac = super().get_mac()
        self.ksDAO = KeystrokeDAO()
        self.running = False
        self.listener = keyboard.Listener(on_release=self.on_release)
        self.listener.start()

    def on_release(self, key):
        if self.running:
            try:
                self.save_keystroke(str(key.char))
            except AttributeError:
                self.save_keystroke(str(key)[4:])

    def save_keystroke(self, key):
        self.ksDAO.create(Keystroke(timestamp=super().get_timestamp(), ip_address=self.ip,
            mac_address=self.mac, annotations=Annotation(self.ip, None).toJSON(), key=key))

    def stop(self):
        self.running = False
    def start(self):
        self.running = True
