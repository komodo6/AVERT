from bson.json_util import dumps
from flask import Blueprint, request
import json

from pymongo import collection
from .Sync import Sync
bp = Blueprint('sync', __name__, url_prefix='/sync')


@bp.route('/', methods=['POST'])
def screenshot_capture():
    collections, ip = request.get_json()
    sync = Sync(ip, collections)

    resp = sync.start_sync()
    return {'msg': resp}, 200