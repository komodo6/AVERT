from flask import Blueprint
from ..Recorder.ProcessRecorder import ProcessRecorder

bp = Blueprint("SystemCall", __name__, url_prefix="/systemcalls")


@bp.route("/")
def index():
    return "das", 200
