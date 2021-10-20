from flask import Blueprint
from ..Recorder.ProcessRecorder import ProcessRecorder
from .SystemCallCapture import SystemCallCapture

bp = Blueprint("SystemCall", __name__, url_prefix="/systemcalls")

active_sys = False

sc = SystemCallCapture()


@bp.route("/")
def get_syscall():
    return "das", 200


@bp.route("/start")
def start_syscall():
    sc.start()

    return "das", 200


@bp.route("/kill")
def kill_syscall():
    sc.stop()

    return "das", 200
