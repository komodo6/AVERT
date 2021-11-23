from .PacketCaptureDAO import PacketCaptureDAO
from .NetworkPacket import NetworkPacket
import datetime
dao = PacketCaptureDAO()
import pyshark
import json


class PacketCaptureService():
    def __init__(self, filename):
        self.filename = filename


    def getPCAPPackets(self, filename):
        packets = dao.getPackets(filename)
        if packets:
            return packets
        else:
            pcapPath = dao.getPacketFile(filename)
            
            self.createPackets(pcapPath, filename)
            




    def createPackets(self, pcapPath, filename):
        # print(pcap.read())
        print(pcapPath)
        cap_raw = pyshark.FileCapture(pcapPath, use_json=True, include_raw=True)
        for packet in cap_raw:
            print(packet)
            pac = self.to_dict(packet)
            raw_hex = str(packet.get_raw_packet())
            
            timestamp = str(datetime.datetime.fromtimestamp(float(pac["sniff_timestamp"])))
            if "tcp.strem" in pac["layers"][2]["_all_fields"]:
                stream = pac["layers"][2]["_all_fields"]["tcp.stream"]
            elif "udp.stream" in pac["layers"][2]["_all_fields"]: 
                stream = pac["layers"][2]["_all_fields"]["udp.stream"]
            np = NetworkPacket(timestamp, rawHexByte=raw_hex, filestream=stream, pcapfileID=filename, packet_data=pac)
            dao.createPacket(self.to_dict(np))
        
        



        



    def to_dict(self, obj):
        return json.loads(json.dumps(obj, default=lambda o: o.__dict__))

