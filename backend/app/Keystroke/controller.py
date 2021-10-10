from flask import Blueprint
import json
from . import KeystrokeDAO
bp = Blueprint('keystrokes', __name__, url_prefix='/keystrokes')

ks = KeystrokeDAO.KeystrokeDAO()



@bp.route('/', methods=['GET'])
def index():
    try:
        all_keystrokes = list(ks.read())
        print(all_keystrokes)
        return json.dumps(all_keystrokes)
        # return list(ks.read())
    except Exception as e:
        print(e)
        return 'error'