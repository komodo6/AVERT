from flask import Blueprint, request
from .WindowHistoryDAO import WindowHistoryDAO
import json


bp = Blueprint("windows", __name__, url_prefix="/windows")
wh = WindowHistoryDAO()


@bp.route("/", methods=['GET'])
def index():
    all_windows = list(wh.read())
    return json.dumps(all_windows), 200


@bp.route('/window', methods=['POST'])
def update_windows_tag():
    id = request.get_json()["id"] if "id" in request.get_json() else None
    if id:
        tags = request.get_json(
        )["tags"] if "tags" in request.get_json() else None
        if tags is not None:
            wh.update_tag(id, tags)
            return "Updated", 200
        else:
            return "Missings tags", 400

    return "Missings id", 400

@bp.route('/count', methods=['GET'])
def get_count_windowhistory():
    try:
        count = wh.get_count()
        print(count)
        return json.dumps(count)
        # return list(ks.read())
    except Exception as e:
        print(e)
        return 'error'
