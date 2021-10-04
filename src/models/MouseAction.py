from Artifact import Artifact

class MouseAction(Artifact):
    def __init__(self, id, timestamp, ip_address, mac_address, annotations):
        super().__init__(id, timestamp, ip_address, mac_address, annotations)

    def __getitem__(self, item):
        return getattr(self, item)
