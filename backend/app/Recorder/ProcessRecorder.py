import psutil
import threading
import time
import sys
import os
from ..models.Process import Process
from .Recorder import Recorder

# sys.path.append('/.../app/models')
# import Process

class ProcessRecorder(Recorder):
    def __init__(self):
        self.pro_dict = {}
    
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
            try:
                for proc in psutil.process_iter():
                    if proc not in self.pro_dict:
                        # Getting all relevant process information
                        new_process = Process(
                            super().get_timestamp,
                            super().get_ip,
                            super().get_mac,
                            None,
                            proc.name(),
                            proc.username(),
                            proc.pid,
                            proc.parent(),
                            proc.create_time(),
                            proc.cmdline(),
                            proc.terminal(),
                            proc.status(),
                            proc.status(),
                            proc.memory_percent(),
                            proc.terminal(),
                            proc.cpu_percent(),
                            os.getuid() == 0,
                            proc.nice()



                        )
                        # get the name of the process
                        # print('Name: ',proc.name())
                        # get user of the process 
                        # print('user: ',proc.username())
                        # get the pid of the process
                        # print('Pid: ',proc.pid)
                        # get the parent of the process
                        # print('Parent: ',proc.parent())
                        # get the start time of the process
                        # print('time:',proc.create_time())
                        # get the command of the process
                        # print('CMD: ',proc.cmdline())
                        # get the terminal of the process
                        # print('Terminal: ',proc.terminal())
                        # get the status of the process
                        # procStat = proc.status()
                        # print('Status:' ,procStat)
                        # get the process type
                        # if procStat == 'running':
                        #     print('Status:', 'foregroundnd')
                        # else:
                        #     print('Status:','background')
                        # get the memory usage of the process
                        # print("Memory: ",proc.memory_percent())
                        # get the Number of threads
                        # print("Threads: ",proc.terminal())
                        # get the cpu percentage
                        # print("Cpu%: " ,proc.cpu_percent())
                        # get process privilges - admin not admin
                        # is_admin = (os.getuid() == 0)
                        # print("Privilges: ",is_admin)
                        # get the process priority
                        # print("Process Priority",proc.nice())
                        # print()
                        
                        self.pro_dict[new_process] = proc.pid
                    else:
                        pass
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        # TODO: put all pro_list into database
        for key in self.pro_dict:
            print(key)
        # putting back pro_list to an empty state
        self.pro_dict = {}
        sys.exit()


if __name__ == '__main__':
    r1 = ProcessRecorder()
    r1.start()
    time.sleep(5)
    r1.stop()

    r1.start()
    time.sleep(5)
    r1.stop()

# def start():
#     global r 
#     r = threading.Thread(target = record)
#     r.start()

# def stop():
#     global r
#     global exit_event
#     exit_event.set()
#     r.join()


# Declaring the global variables    
# global pro_list
# global exit_event
# global r

# init some stuff
# pro_list = {}
# exit_event = threading.Event()

# Making the thread and starting the thread
# start()

# # Stop for a bit 
# time.sleep(10)
# stop()


# # Making sure pro_list is empty
# print()
# print ('pro:', pro_list)


