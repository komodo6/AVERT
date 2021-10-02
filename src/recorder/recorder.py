import socket
import time
import uuid
import re


def get_ip():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    return ip_address


def get_mac():
    mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return mac_address


def get_timestamp():
    time_stamp = time.time()
    return time_stamp
