from bson.json_util import dumps
import re
from flask import Blueprint, send_file, render_template, request, make_response
import json
import os
import bson
from werkzeug.wsgi import ClosingIterator, wrap_file
from .VideoCapture import VideoCapture
from .VideoDAO import VideoDAO
bp = Blueprint('videos', __name__, url_prefix='/videos')

# Getting vids
vdao = VideoDAO()

current_dir = os.path.dirname(os.path.abspath(__file__))


@bp.route('/capture', methods=['GET'])
def start_recording():
    # TODO: 
    # import capture videop
    print('in capture')
    cs = VideoCapture()
    # start here
    cs.start()
    return 'capture',200

@bp.route('/stop', methods=['GET'])
def stop_recording(cs):
    # TODO: 
    # import capture videop
    cs = VideoCapture
    # stop here
    cs.stop()
    print('in stop')
 


@bp.route('/videos', methods=['GET'])
def get_images():
    videos = list(vdao.read_all())
    return dumps(videos)


@bp.route('/video', methods=['GET'])
def get_image():
    img = request.args.get("id") if "id" in request.args else None
    if img:
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        path = os.path.join(current_dir,f"./videos/{id}.mp4")
        
        
        resp = make_response(send_file(path))
        resp.headers['Content-Disposition'] = 'inline'
        return resp
        # return send_file(path, 'video/mp4')

    else:
        return "Image does not exist", 404


@bp.route('/image', methods=['POST'])
def update_image():

    id = request.get_json()["id"] if "id" in request.get_json() else None
    if id:
        tags = request.get_json(
        )["tags"] if "tags" in request.get_json() else None
        if tags is not None:
            dao.update_tag(id, tags)
            return "Updated", 200
        else:
            return "Missings tags", 400

    return "Missings id", 400


