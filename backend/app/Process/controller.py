from flask import Blueprint, request
from .ProcessDAO import ProcessDAO
import json


bp = Blueprint("process", __name__, url_prefix="/processes")
ps = ProcessDAO()


@bp.route("/", methods=['GET'])
def index():
    all_processes = list(ps.read())
    return json.dumps(all_processes), 200


@bp.route('/process', methods=['POST'])
def update_mouseaction_tag():
    id = request.get_json()["id"] if "id" in request.get_json() else None
    if id:
        tags = request.get_json(
        )["tags"] if "tags" in request.get_json() else None
        if tags is not None:
            ps.update_tag(id, tags)
            return "Updated", 200
        else:
            return "Missings tags", 400

    return "Missings id", 400

@bp.route('/count', methods=['GET'])
def get_count_processes():
    try:
        count = ps.get_count()
        print(count)
        return json.dumps(count)
        # return list(ks.read())
    except Exception as e:
        print(e)
        return 'error'