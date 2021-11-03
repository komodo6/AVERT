from ..models.Artifact import Artifact

class NetworkData(Artifact):
    def __init__(self, timestamp, ip_address, mac_address, annotations, tags, pcapfile=None, startTime=None, endTime=None):
        super().__init__(timestamp, ip_address, mac_address, annotations, tags)
        self.pcapfile = pcapfile
        self.startTime = startTime
        self.endTime = endTime


    def __getitem__(self, item):
        return getattr(self, item)
