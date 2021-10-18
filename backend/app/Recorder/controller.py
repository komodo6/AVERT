from flask import Blueprint
from .ProcessRecorder import ProcessRecorder
import sys
bp = Blueprint('recording', __name__, url_prefix='/recording')


p_rec = ProcessRecorder()

@bp.route('/process/start')
def start_recording_proc():
    p_rec.start()
    print('test', file=sys.stderr)
    return ('<h1>i did something</h1>', 200)

@bp.route('/process/stop')
def stop_recording_proc():
    p_rec.stop()
    print('stopping')
    return('Stopping', 200)