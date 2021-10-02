from Artifact import Artifact

class MouseActions(Artifact):
    def __init__(self, timestamp, ip_address, mac_address, annotations):
        super().__init__(timestamp, ip_address, mac_address, annotations)



    def __getitem__(self, item):
        return getattr(self, item)
