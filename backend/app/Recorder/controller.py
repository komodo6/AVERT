from flask import Blueprint, request
import json
from .KeystrokeRecorder import KeystrokeRecorder
from .MouseActionRecorder import MouseActionRecorder

bp = Blueprint('recording', __name__, url_prefix='/recording')

recorders = {'keystrokes': KeystrokeRecorder(), 'cursor': MouseActionRecorder()}

@bp.route('/', methods=['POST'])
def index():
    try:
        toggle, rec_type = request.get_json().values()

        recorder = recorders[rec_type]

        if toggle:
            recorder.start()
        elif not toggle:
            recorder.stop()
        return json.dumps({'msg': 'ok'})
    except Exception as e:
        print(e)
        return 'error'