from threading import Thread
import pyshark
import json
from .NetworkData import NetworkData
from .PacketCaptureDAO import PacketCaptureDAO
import uuid
import os
import datetime
import time
import subprocess 
from ..Recorder.Recorder import Recorder
r = Recorder()
class PacketCapture(Thread):
    capture = 1
    def __init__(self, interface_name):
        self.nd = NetworkData(r.get_timestamp(), r.get_ip(),
                           r.get_mac(), [], [])
        self.interface_name = interface_name
        self.dao = PacketCaptureDAO()
        Thread.__init__(self)


    def stop(self):
        self.capture = 0
        


    def run(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        id = str(uuid.uuid4())
        self.nd.pcapfile = f"{id}.pcap"
        self.nd.startTime = str(datetime.datetime.utcnow())
        pcapPath = os.path.join(current_dir, f"../pcaps/{id}.pcap")
        
        # capture = pyshark.LiveCapture(interface=self.interface_name, use_json=True, include_raw=True, output_file=pcapPath)
        try:
            tcpdump = subprocess.Popen(["tcpdump", "-w", f"{pcapPath}"])
            while tcpdump.poll() is None:
                if not self.capture:
                    tcpdump.terminate()
                    time.sleep(2)
                    self.nd.endTime = str(datetime.datetime.utcnow())
                    self.dao.createPCAP(self.nd)
                    break
            print("Drone")
            
                    
            
            # for packet in capture.sniff_continuously():
            #     print("fff")
            #     print(packet)
            #     if not self.capture:
                    # capture.close()
            print("Drone")
            
            return
        except pyshark.capture.capture.TSharkCrashException:
            self.exited = 1
            print("Capture has crashed")
   

