import uuid

class Artifact:        
    def __init__(self, timestamp, ip_address, mac_address, annotations, tags):
        self.id = str(uuid.uuid1())
        self.timestamp = timestamp
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.annotations = annotations
        self.tags = tags

    def __getitem__(self, item):
        return getattr(self, item)


    def toJSON(self):
        return self.__dict__

       
