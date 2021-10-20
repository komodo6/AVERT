from flask import Blueprint, request
import json
from .KeystrokeRecorder import KeystrokeRecorder
from .MouseActionRecorder import MouseActionRecorder
from .ProcessRecorder import ProcessRecorder
from .WindowHistoryRecorder import WindowHistoryRecorder

bp = Blueprint('recording', __name__, url_prefix='/recording')

recorders = {'keystrokes': KeystrokeRecorder(), 'mouse': MouseActionRecorder(), 'processes': ProcessRecorder()}

wh = WindowHistoryRecorder()
@bp.route('/window_history/start', methods=['GET'])
def window_start():
    wh.start()
    return ('start', 200)

@bp.route('/window_history/stop', methods=['GET'])
def window_stop():
    wh.stop()
    return ('start', 200)
    
@bp.route('/', methods=['POST'])
def index():
    try:
        toggles = request.get_json()

        print(toggles)

        for key in toggles:
            if toggles[key] and key in recorders:
                recorders[key].start()
            elif not toggles[key] and key in recorders:
                recorders[key].stop()

        return json.dumps({'msg': 'ok'})
    except Exception as e:
        print(e)
        return 'error'
