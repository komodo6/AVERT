from src.models.Artifact import Artifact

class MouseActions(Artifact):
    def __init__(self, timestamp, ip_address, mac_address, annotations):
        super().__init__(timestamp, ip_address, mac_address, annotations)
        self.type = ""
        self.coords = []
        self.pressed = False
        self.button = ""

    def __getitem__(self, item):
        return getattr(self, item)
