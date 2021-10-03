import pynput
from src.models.Keystroke import Keystroke
from src.models.recorder import Recorder


class KeystrokeRecorder(Recorder):
    def __init__(self):
        self.listener = pynput.keyboard.Listener(on_release=self.on_release)
        self.listener.start()
        self.listener.join()

    def on_release(self, key):
        try:
            self.save_keystroke(str(key.char))
        except AttributeError:
            self.save_keystroke(str(key)[4:])

    def save_keystroke(self, key):
        time = None
        ip = None
        mac = None
        Keystroke(key, time, ip, mac, [])

    def stop(self):
        self.listener.stop()
        
    def start(self):
        self.listener.start()
