from flask import Blueprint, request
import json
from . import KeystrokeDAO
import datetime
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


@bp.route('/tags', methods=['POST'])
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

@bp.route('/count', methods=['GET'])
def get_count_keystrokes():
    try:
        count = ks.get_count()
        print(count)
        return json.dumps(count)
        # return list(ks.read())
    except Exception as e:
        print(e)
        return 'error'


@bp.route('/annotations', methods=['POST'])
def update_annotation():
    id = request.get_json()["id"] if "id" in request.get_json() else None
    if id:
        annotation = request.get_json(
        )["annotation"] if "annotation" in request.get_json() else None
        if annotation is not None:
            ks.update_annotation(id, annotation)
            return "Updated", 200
        else:
            return "Missings annotation", 400

    return "Missings id", 400


@bp.route('/timeline', methods=['POST'])
def get_keystrokes_timeline():
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
        r_intervals = r_intervals + [len(ks.read_time_interval(start_date))]
        start_date =  start_date + increment

    print(r_times)
    print(r_intervals)
    r = {'r_times':r_times, 'r_intervals':r_intervals}
          

    
    

    # id = request.get_json()["id"] if "id" in request.get_json() else None
    # if id:
    #     tags = request.get_json(
    #     )["tags"] if "tags" in request.get_json() else None
    #     if tags is not None:
    #         ma.update_tag(id, tags)
    #         return "Updated", 200
    #     else:
    #         return "Missings tags", 400

    return json.dumps(r), 200


