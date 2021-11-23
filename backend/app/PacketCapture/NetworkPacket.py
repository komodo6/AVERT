from ..models.Artifact import Artifact

class NetworkPacket():
    def __init__(self, timestamp, rawHexByte, packet_data, filestream, pcapfileID):
        self.timestamp = timestamp
        self.rawHexByte = rawHexByte
        self.pcapfileID = pcapfileID
        self.packet_data = packet_data
        self.filestream = filestream
        

    def __getitem__(self, item):
        return getattr(self, item)


    
        
