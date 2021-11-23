from .Recorder import Recorder
from app.Keystroke.KeystrokeDAO import KeystrokeDAO
from pynput import keyboard
from app.models.Keystroke import Keystroke
from app.models.Annotation import Annotation

# import gi
# gi.require_version('Gtk', '3.0')
# gi.require_version('Wnck', '3.0')
# from gi.repository import Gtk, Wnck
# from services.ActiveWindow import ActiveWindow

class KeystrokeRecorder(Recorder):
    def __init__(self) -> None:
        super().__init__()
        self.k_list = []
        self.ip = super().get_ip()
        self.mac = super().get_mac()
        self.ksDAO = KeystrokeDAO()
        self.running = False
        self.listener = keyboard.Listener(on_release=self.on_release)
        self.listener.start()
        # self.aw = ActiveWindow()
        # self.aw.start()
        # Gtk.main()

    def on_release(self, key):
        if self.running:
            key = '{}'.format(key)
            print(key)
            self.k_list = self.k_list + [{'timestamp': super().get_timestamp(), 'ip': self.ip, 'mac':self.mac, 'annotations':[] , 'tags':[], 'key':key, 'active_window':None}]
            # print("k_lis on_release: ",self.k_list)
            # try:
            #     self.save_keystroke(str(key.char))
            # except AttributeError:
            #     self.save_keystroke(str(key)[4:])

    # def save_keystroke(self, key):
    #     a = Annotation(self.ip, None)
    #     self.ksDAO.create(Keystroke(timestamp=super().get_timestamp(), ip_address=self.ip,
    #                                 mac_address=self.mac, annotations=[], tags=[], key=key, active_window=None))

    def stop(self):
        self.running = False
        # print(self.k_list)
        sum = 0
        for k in self.k_list:
            # print(k)
            keystroke = Keystroke(k['timestamp'], ip_address=k['ip'],mac_address=k['mac'], annotations=k['annotations'], tags=k['tags'], key=k['key'], active_window=k['active_window'])    
            self.ksDAO.create(keystroke)
            
        # for k in self.k_list:
        #     print(k)
            # keystroke = Keystroke(k['timestamp'], ip_address=k['ip'],mac_address=k['mac'], annotations=k['annotations'], tags=k['tags'], key=k['key'], active_window=k['active_window'])
        #     # keystroke = Keystroke(timestamp=super().get_timestamp(), ip_address=self.ip,mac_address=self.mac, annotations=[], tags=[], key=key, active_window=None)
        #     self.ksDAO.create(keystroke)
        self.k_list = []

    def start(self):
        self.running = True

    def getWindow(self, screen, previous_window):
        try:
            return screen.get_active_window().get_name()
        except AttributeError:
            pass
