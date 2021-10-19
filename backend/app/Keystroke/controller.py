from flask import Blueprint, request
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


@bp.route('/keystroke', methods=['POST'])
def update_keystroke_tag():
    id = request.get_json()["id"] if "id" in request.get_json() else None
    if id:
        tags = request.get_json(
        )["tags"] if "tags" in request.get_json() else None
        if tags is not None:
            ks.update_tag(id, tags)
            return "Updated", 200
        else:
            return "Missings tags", 400

    return "Missings id", 400
