from .Artifact import Artifact

class WindowHistory(Artifact):
    def __init__(self, timestamp, ip_address, mac_address, annotations, tags,
    screen_res

    ):
        super().__init__(timestamp, ip_address, mac_address, annotations, tags)
        self.screen_res = screen_res
    

