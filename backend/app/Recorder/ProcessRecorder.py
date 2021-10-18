import psutil
import threading
import time
import sys
import signal
import os
import ctypes


# Iterate over all running process
def record():
    global pro_list
    global thread_id

    # Checking  if thread should stop
    while not exit_event.is_set():
    # Finding all processes
        try:
            for proc in psutil.process_iter():
                if proc not in pro_list:
                    # Getting all relevant process information

                    # get the name of the process
                    print('Name: ',proc.name())
                    '''
                    # get user of the process 
                    print('user: ',proc.username())
                    # get the pid of the process
                    print('Pid: ',proc.pid)
                    # get the parent of the process
                    print('Parent: ',proc.parent())
                    # get the start time of the process
                    print('time:',proc.create_time())
                    # get the command of the process
                    print('CMD: ',proc.cmdline())
                    # get the terminal of the process
                    print('Terminal: ',proc.terminal())
                    # get the status of the process
                    procStat = proc.status()
                    print('Status:' ,procStat)
                    # get the process type
                    if proc.status == 'running':
                        print('Status:', 'foregroundnd')
                    else:
                        print('Status:','background')
                    # get the memory usage of the process
                    print("Memory: ",proc.memory_percent())
                    # get the Number of threads
                    print("Threads: ",proc.terminal())
                    # get the cpu percentage
                    print("Cpu%: " ,proc.cpu_percent())
                    # get process privilges - admin not admin
                    is_admin = (os.getuid() == 0)
                    print("Privilges: ",is_admin)
                    # get the process priority
                    print("Process Priority",proc.nice())
                    '''
                    print()
                    
                    pro_list[proc] = proc.pid
                else:
                    pass
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    # TODO: put all pro_list into database
    for key in pro_list:
        print(key)
    # putting back pro_list to an empty state
    pro_list = {}
    sys.exit()

def start():
    global r 
    r = threading.Thread(target = record)
    r.start()

def stop():
    global r
    global exit_event
    exit_event.set()
    r.join()


# Declaring the global variables    
global pro_list
global exit_event
global r

# init some stuff
pro_list = {}
exit_event = threading.Event()

# Making the thread and starting the thread
start()

# Stop for a bit 
time.sleep(10)
stop()


# Making sure pro_list is empty
print()
print ('pro:', pro_list)


