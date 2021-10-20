import psutil
import os
import subprocess
from threading import Thread, Event
import time
from .SystemCallDAO import SystemCallDAO
from ..models.SystemCall import SystemCall
from ..Recorder.Recorder import Recorder
import re
import os
import signal

mypid = os.getpid()
all_pids = []
ignore_pids = []
ignore_pids.append(mypid)


scd = SystemCallDAO()
r = Recorder()

allThreads = []
processes = []


class SystemCallCapture(Thread):
    def __init__(self):
        Thread.__init__(self)
        self._stop_event = Event()

    def run(self):

        while True:
            for p in psutil.process_iter():
                pid = p.as_dict()["pid"]
                print("das")
                # checks if its strace or python process
                if pid not in ignore_pids:
                    # checks if new pid
                    if pid not in all_pids:
                        thread = Thread(target=self.start_strace, args=(pid,))
                        thread.start()
                        # thread.join()

            time.sleep(1)
            if self.stopped():
                for p in processes:
                    print(p.pid)
                    p.send_signal(signal.SIGKILL)
                # for p in ignore_pids[1:]:
                #     print(p)
                #     os.killpg(os.getpgid(p), signal.SIGTERM)
                break

    def start_strace(self, pid):
        all_pids.append(pid)
        strace = subprocess.Popen(
            ["strace", "-p", f"{pid}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ignore_pids.append(strace.pid)
        if strace.poll() is None:
            tr = self._stop_event
            pt = Thread(target=self.stream_process, args=(strace, pid, tr))
            pt.start()
            allThreads.append(pt)
            processes.append(strace)

        else:
            strace.send_signal(signal.SIGTERM)
            try:
                all_pids.remove(pid)
            except ValueError:
                pass
            try:
                ignore_pids.remove(strace.pid)
            except ValueError:
                pass

    def stream_process(self, process, pid, tr):
        if process.poll() is not None:
            ignore_pids.remove(process.pid)
            all_pids.remove(pid)
            return
        # if(tr.isSet()):
        #     process.send_signal(signal.CTRL_C_EVENT)
        #     print('das')
        #     for t in allThreads:
        #         print("das")
        #         t.join()

        for line in process.stderr:
            sys_call = line.decode('utf-8').strip()
            # print(sys_call)
            pattern = re.compile(r"(.*?)\(.*\"(.*?)\".*=(.*)")

            match = pattern.match(sys_call)
            if match is None:
                continue
            else:
                sys_call_name = match.groups()[0].strip()
                sys_call_args = match.groups()[1].strip()
                sys_call_retval = match.groups()[2].strip()

            s = SystemCall(r.get_timestamp(), r.get_ip(),
                           r.get_mac(), [], [], sys_call_name, sys_call_args, sys_call_retval, None)
            scd.create(s)

    def kill(self):
        self._kill.set()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
