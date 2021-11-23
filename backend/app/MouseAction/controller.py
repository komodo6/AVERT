from flask import Blueprint, request
import json
from . import MouseActionsDAO

bp = Blueprint('mouseactions', __name__, url_prefix='/mouseactions')

ma = MouseActionsDAO.MouseActionsDAO()


@bp.route('/', methods=['GET'])
def index():
    all_mouseactions = list(ma.read())
    return json.dumps(all_mouseactions)


@bp.route('/mouseaction', methods=['POST'])
def update_mouseaction_tag():
    id = request.get_json()["id"] if "id" in request.get_json() else None
    if id:
        tags = request.get_json(
        )["tags"] if "tags" in request.get_json() else None
        if tags is not None:
            ma.update_tag(id, tags)
            return "Updated", 200
        else:
            return "Missings tags", 400

    return "Missings id", 400


@bp.route('/count', methods=['GET'])
def get_count_mouseactions():
    try:
        count = ma.get_count()
        print(count)
        return json.dumps(count)
        # return list(ks.read())
    except Exception as e:
        print(e)
        return 'error'