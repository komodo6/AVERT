from bson.json_util import dumps
import re
from flask import Blueprint, send_file, render_template, request, make_response
import json
import os
import bson
from werkzeug.wsgi import ClosingIterator, wrap_file
from .VideoCapture import VideoCapture
from .VideoDAO import VideoDAO
import datetime
bp = Blueprint('videos', __name__, url_prefix='/videos')

# Getting vids
vdao = VideoDAO()

current_dir = os.path.dirname(os.path.abspath(__file__))

global videoOFF, cs

videoOFF = True

@bp.route('/capture', methods=['GET'])
def start_recording():
    global videoOFF, cs
    if videoOFF:
        cs = VideoCapture()
        cs.start()
        videoOFF = False
        return "capturing"
    else:
        videoOFF = True
        cs.stop()
        return "Stopped reoording"
        
    # TODO: 
    # import capture videop
    print('in capture')
    
    # start here
    cs.start()
    return('capture',200)

@bp.route('/stop', methods=['GET'])
def stop_recording():
    global videoOFF, cs
    # TODO: 
    # import capture videop
    #cs = VideoCapture
    # stop here
    cs.stop()
    videoOFF = True
    print('in stop')
    return('stop',200)
 


@bp.route('/', methods=['GET'])
def get_images():
    videos = list(vdao.read_all())
    return dumps(videos)


@bp.route('/video', methods=['GET'])
def get_image():
    img = request.args.get("id") if "id" in request.args else None
    if img:
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(img)
        
        path = os.path.join(current_dir,f"./videos/{img}")
        
        
        resp = make_response(send_file(path))
        resp.headers['Content-Disposition'] = 'inline'
        return resp
        # return send_file(path, 'video/mp4')

    else:
        return "Image does not exist", 404


@bp.route('/tags', methods=['POST'])
def update_image():

    id = request.get_json()["id"] if "id" in request.get_json() else None
    if id:
        tags = request.get_json(
        )["tags"] if "tags" in request.get_json() else None
        if tags is not None:
            vdao.update_tag(id, tags)
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
            vdao.update_annotation(id, annotation)
            return "Updated", 200
        else:
            return "Missings annotation", 400

    return "Missings id", 400


@bp.route('/video', methods=['DELETE'])
def remove_image():

    id = request.args.get("id") if "id" in request.args else None
    if id:
        vdao.delete(id)
        return f"removed, {id}", 200

    return "Missings id", 400

@bp.route('/count', methods=['GET'])
def get_count_videos():
    try:
        count = vdao.get_count()
        print(count)
        return json.dumps(count)
        # return list(ks.read())
    except Exception as e:
        print(e)
        return 'error'


@bp.route('/timeline', methods=['POST'])
def get_videos_timeline():
    print('Made it in get_mouse)action')
    time_range = request.get_json()

    print(time_range['start']) # TODO:Delete
    print(time_range['end'])
    start_date = datetime.datetime.strptime(time_range['start'],"%Y-%m-%d %H:%M:%S.%f")
    end_date = datetime.datetime.strptime(time_range['end'],"%Y-%m-%d %H:%M:%S.%f")
    increment = datetime.timedelta(milliseconds=100)
    r_times = []
    r_intervals = []

    while start_date <= end_date:
        r_times = r_times + [start_date.strftime("%Y-%m-%d %H:%M:%S.%f")]
        r_intervals = r_intervals + [len(vdao .read_time_interval(start_date))]
        start_date =  start_date + increment

    print(r_times)
    print(r_intervals)
    r = {'r_times':r_times, 'r_intervals':r_intervals}

    return json.dumps(r), 200
