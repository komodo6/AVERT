import pyshark
import json
import scapy
import pprint
capture = pyshark.FileCapture("./cap.pcap", use_json=True, include_raw=True)

def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))

print(capture[0].get_raw_packet())
# for packet in capture:
#     print(to_dict(packet)["layers"][2]["_all_fields"].keys())
#     pprint.pprint(to_dict(packet))



# from scapy.all import *

# def pkt_callback(pkt):
#     pkt.show() # debug statement

# sniff()