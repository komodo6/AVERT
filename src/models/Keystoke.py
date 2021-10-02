import json

from Artifact import Artifact

class Keystroke(Artifact):
    
    def __init__(self, timestamp, ip_address, mac_address, annotations, key):
        super().__init__(timestamp, ip_address, mac_address, annotations)
        self.key = key


    def __getitem__(self, item):
        return getattr(self, item)
