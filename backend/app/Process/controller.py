from flask import Blueprint, request
from .ProcessDAO import ProcessDAO
import json


bp = Blueprint("process", __name__, url_prefix="/processes")
ps = ProcessDAO()


@bp.route("/", methods=['GET'])
def index():
    all_processes = list(ps.read())
    return json.dumps(all_processes), 200


@bp.route('/tags', methods=['POST'])
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

@bp.route('/annotations', methods=['POST'])
def update_annotation():
    id = request.get_json()["id"] if "id" in request.get_json() else None
    if id:
        annotation = request.get_json(
        )["annotation"] if "annotation" in request.get_json() else None
        if annotation is not None:
            ps.update_annotation(id, annotation)
            return "Updated", 200
        else:
            return "Missings annotation", 400

    return "Missings id", 400