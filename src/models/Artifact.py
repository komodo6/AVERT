import uuid
class Artifact:        
    def __init__(self, timestamp, ip_address, mac_address, annotations):
        self.id = uuid.uuid1()
        self.timestamp = timestamp
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.annotations = annotations

    def __getitem__(self, item):
        return getattr(self, item)


    def toJSON(self):
        return self.__dict__

       
