from flask import Blueprint
from ..Recorder.ProcessRecorder import ProcessRecorder

bp = Blueprint("process", __name__, url_prefix="/processes")


@bp.route("/")
def index():
    return "das", 200
