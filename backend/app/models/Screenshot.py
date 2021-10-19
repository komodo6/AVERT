from .Artifact import Artifact


class Screenshot(Artifact):
    def __init__(self, timestamp, ip_address, mac_address, annotations, tags, ScreenshotFile, ScreenshotSize, ScreenshotFormat):
        super().__init__(timestamp, ip_address, mac_address, annotations, tags)
        self.ScreenshotFile = ScreenshotFile
        self.ScreenshotSize = ScreenshotSize
        self.ScreenshotFormat = ScreenshotFormat

    def toJSON(self):
        return super().toJSON()
