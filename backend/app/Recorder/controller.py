from flask import Blueprint, request
import json
from .KeystrokeRecorder import KeystrokeRecorder
from .MouseActionRecorder import MouseActionRecorder
from .ProcessRecorder import ProcessRecorder
from .WindowHistoryRecorder import WindowHistoryRecorder

bp = Blueprint('recording', __name__, url_prefix='/recording')

recorders = {'keystrokes': KeystrokeRecorder(), 'mouse': MouseActionRecorder(), 'processes': ProcessRecorder(), 'window_history': WindowHistoryRecorder()}
    
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
