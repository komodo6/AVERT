import socket
import time
import uuid
import re
import datetime

class Recorder:

    def get_ip(self):
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address

    def get_mac(self):
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        return mac_address

    def get_timestamp(self):
        time_stamp = datetime.datetime.utcnow()
        return time_stamp

