import psutil
import os
import subprocess
from threading import Thread
import time
import re


mypid = os.getpid()
all_pids = []
ignore_pids = []
ignore_pids.append(mypid)


def stream_process(process, pid):
    if process.poll() is not None:
        ignore_pids.remove(process.pid)
        all_pids.remove(pid)
        return
    for line in process.stderr:
        sys_call = str(line.decode('utf-8'))
        with open("t.txt", "a") as f:
            f.write(sys_call)

        pattern = re.compile(r"(.*?)\(.*\"(.*?)\".*=(.*)")

        match = pattern.match(sys_call)
        if match is None:
            continue
        else:
            print(match.groups()[0])
            print(match.groups()[1])
            print(match.groups()[2])


def start_strace(pid):
    all_pids.append(pid)
    strace = subprocess.Popen(
        ["strace", "-f", "-p", f"{pid}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ignore_pids.append(strace.pid)
    if strace.poll() is None:
        pt = Thread(target=stream_process, args=(strace, pid,))
        pt.start()
    else:
        try:
            all_pids.remove(pid)
        except ValueError:
            pass
        try:
            ignore_pids.remove(strace.pid)
        except ValueError:
            pass


while True:
    for p in psutil.process_iter():
        pid = p.as_dict()["pid"]
        # checks if its strace or python process
        if pid not in ignore_pids:
            # checks if new pid
            if pid not in all_pids:
                thread = Thread(target=start_strace, args=(pid,))
                thread.start()
                thread.join()

    time.sleep(1)
