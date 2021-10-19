from .Artifact import Artifact
class Screenshot(Artifact):

    def __init__(self, timestamp, ip_address, mac_address, annotations, active_window, image_id):
        super().__init__(timestamp, ip_address, mac_address, annotations, active_window)
        self.image_id = image_id


    def toJSON(self):
        return super().toJSON()