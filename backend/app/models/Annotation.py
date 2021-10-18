class Annotation:
    def __init__(self, ip_address, note) -> None:
        self.ip_address = ip_address
        self.note = note

    def __getitem__(self, item):
        return getattr(self, item)

    def toJSON(self):
        return self.__dict__