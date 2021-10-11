from models.Artifact import Artifact

import io

class Screenshot(Artifact):
    def __init__(self, timestamp, ip_address, mac_address, annotations, image):
        super().__init__(timestamp, ip_address, mac_address, annotations, active_window=None)
        self.format = 'PNG'
        self.image = image

    def change_format(self,format):
        self.format = format

    def save(self):
        image_bytes = io.BytesIO()
        self.image.save(image_bytes, format=self.format)
