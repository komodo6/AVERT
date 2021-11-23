from .Artifact import Artifact


class Video(Artifact):
    def __init__(self, timestamp, ip_address, mac_address, annotations, tags, resolution, frameRate, filename):
        super().__init__(timestamp, ip_address, mac_address, annotations, tags)
        self.resolution = resolution
        self.frameRate = frameRate
        self.filename = filename

    def toJSON(self):
        return super().toJSON()
