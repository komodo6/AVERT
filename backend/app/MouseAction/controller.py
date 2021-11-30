from flask import Blueprint, request
import json
from . import MouseActionsDAO
import datetime


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

@bp.route('/timeline', methods=['POST'])
def get_mouseaction_timeline():
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
        r_intervals = r_intervals + [len(ma.read_time_interval(start_date))]
        start_date =  start_date + increment

    print(r_times)
    print(r_intervals)
    r = {'r_times':r_times, 'r_intervals':r_intervals}

    return json.dumps(r), 200


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