import json
from models.Artifact import Artifact

class Keystroke(Artifact):

    def __init__(self, id, timestamp, ip_address, mac_address, annotations, key):
        super().__init__(id, timestamp, ip_address, mac_address, annotations)
        self.key = key
    

    def __getitem__(self, item):
        return getattr(self, item)


    
        