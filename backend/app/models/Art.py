import uuid
import datetime
import socket
import re
class Artifact:        
    id = str(uuid.uuid1())
    timestamp = str(self.get_timestamp())
    ip_address = self.get_ip()
    mac_address = self.get_mac()
    annotations = []
    tags = []
    def __init__(self, annotations, tags):
        

    def __getitem__(self, item):
        return getattr(self, item)


    def toJSON(self):
        return self.__dict__


    def get_ip(self):
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address

    def get_mac(self):
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        return mac_address

    def get_timestamp(self):
        time_stamp = datetime.datetime.utcnow()
        return str(time_stamp)

       
