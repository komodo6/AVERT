from .Artifact import Artifact

class Process(Artifact):
    def __init__(self, timestamp, ip_address, mac_address, annotations,
    proc_name,
    proc_user,
    proc_pid,
    proc_parent,
    proc_time_created,
    proc_cmdline,
    proc_terminal,
    proc_status,
    proc_type,
    proc_memory_percentage,
    proc_threads,
    proc_cpu_percentage,
    proc_privileges,
    proc_priority
    ):
        super().__init__(timestamp, ip_address, mac_address, annotations,None)
        self.proc_name = proc_name
        self.proc_user = proc_user
        self.proc_pid = proc_pid
        self.proc_parent = proc_parent
        self.proc_time_created = proc_time_created
        self.proc_cmdline = proc_cmdline
        self.proc_terminal = proc_terminal
        self.proc_status = proc_status
        
        if proc_type == 'running':
            self.proc_type = 'Foreground'
        else:
            self.proc_type = 'Background'

        self.proc_memory_percentage = proc_memory_percentage
        self.threads = proc_threads
        self.proc_cpu_precentage = proc_cpu_percentage

        if proc_privileges == True:
            self.proc_privileges = 'Admin'
        else:
            self.proc_privileges = 'Not Admin'
        
        self.proc_priority = proc_priority
    

