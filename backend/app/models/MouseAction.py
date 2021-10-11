from models.Artifact import Artifact

class MouseAction(Artifact):
    def __init__(self, timestamp, ip_address, mac_address, annotations,
                 type="", coord_x=None, coord_y=None, pressed=False, button="", scroll=0, active_window=None,):
        super().__init__(timestamp, ip_address, mac_address, annotations, active_window)
        self.type = type
        self.coords = [coord_x, coord_y]
        self.pressed = pressed
        self.button = button
        self.scroll = scroll

    def __getitem__(self, item):
        return getattr(self, item)