from flask import Blueprint, request
from ..Recorder.ProcessRecorder import ProcessRecorder
from .SystemCallCapture import SystemCallCapture
from .SystemCallDAO import SystemCallDAO
import json

bp = Blueprint("SystemCall", __name__, url_prefix="/systemcalls")

active_sys = False

sc = SystemCallCapture()

scd = SystemCallDAO()


@bp.route("/")
def get_syscall():
    d = list(scd.read())

    return json.dumps(d), 200


@bp.route("/start")
def start_syscall():
    sc.start()
    return "das", 200


@bp.route("/kill")
def kill_syscall():
    sc.stop()
    return "das", 200


@bp.route('/tags', methods=['POST'])
def update_image():

    id = request.get_json()["id"] if "id" in request.get_json() else None
    if id:
        tags = request.get_json(
        )["tags"] if "tags" in request.get_json() else None
        if tags is not None:
            scd.update_tag(id, tags)
            return "Updated", 200
        else:
            return "Missings tags", 400

    return "Missings id", 400


@bp.route('/systemcall/<id>', methods=['DELETE'])
def delete_image(id):
    img = id
    if img:
        scd.delete(img)
        return img, 200
    else:
        return "Image does not exist", 404
