import psutil

# Iterate over all running process

for proc in psutil.process_iter():
    try:
        print(type(proc))
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        print(processName, ' ::: ', processID)
        # get user of the process 
        # get the name of the process
        # get the pid of the process
        # get the parent of the process
        # get the start time of the process
        # get the command of the process
        # get the terminal of the process
        # get the status of the process
        # get the memory usage of the process
        # get the Number of threads
        # get the cpu percentage
        # get process privilges - admin not admin
        # get the process priority
        # get the process type
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
