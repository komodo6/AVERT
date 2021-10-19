class Annotation:
    def __init__(self, ip_address) -> None:
        self.ip_address = ip_address
        self.annotations = []

    def add_annotations(self, ip, text):
        #TODO: maybe add get a new ip if someone else makes an annotation
        self.annotations = self.annotations + [{'ip':ip,'text':text}]

    def __getitem__(self, item):
        return getattr(self, item)

    def toJSON(self):
        return self.__dict__

    
if __name__ == '__main__':
    ann = Annotation('1.1.1.1')
    ann.add_annotations(ann.ip_address, 'this is text1')
    ann.add_annotations(ann.ip_address, 'this is text2')
    ann.add_annotations(ann.ip_address, 'this is text3SS')
    print(ann.toJSON())
