import psutil
import threading
import time
import sys
import os
from ..models.Process import Process
from ..Process.ProcessDAO import ProcessDAO
from .Recorder import Recorder

class ProcessRecorder(Recorder):
    def __init__(self):
        self.pro_dict = {}
        self.process_collection = ProcessDAO()
    
    def start(self):
        self.exit_event = threading.Event()
        self.r = threading.Thread(target = self.record)
        self.r.start()
    
    def stop(self):
        self.exit_event.set()
        self.r.join()
    
    def record(self):
        # Checking  if thread should stop
        while not self.exit_event.is_set():
        # Finding all processes
            for proc in psutil.process_iter():
                try:
                    if proc not in self.pro_dict:
                        # Getting all relevant process information
                        new_process = Process(
                            super().get_timestamp(),
                            super().get_ip(),
                            super().get_mac(),
                            [],
                            [],
                            proc.name(),
                            proc.username(),
                            proc.pid,
                            proc.ppid(),
                            proc.create_time(),
                            proc.cmdline(),
                            None,
                            proc.status(),
                            proc.status(),
                            proc.memory_percent(),
                            proc.threads(),
                            proc.cpu_percent(),
                            None,
                            proc.nice()
                        )
                        self.process_collection.create(new_process)
                        self.pro_dict[new_process] = proc.pid
                    else:
                        pass
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        self.pro_dict = {}
        sys.exit()



