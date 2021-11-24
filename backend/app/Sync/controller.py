from bson.json_util import dumps
from flask import Blueprint, request
import json
from .Sync import Sync
bp = Blueprint('sync', __name__, url_prefix='/sync')


@bp.route('/', methods=['POST'])
def screenshot_capture():
    ip = request.args.get("ip") if "ip" in request.args else None
    collections = request.args.get("collections") if "collections" in request.args else None
    sync = Sync(ip, collections)

    resp = sync.start_sync()
    return {'msg': resp}, 200