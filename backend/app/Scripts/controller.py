from flask import Blueprint, request
# from .ProcessDAO import ProcessDAO
from .scripting import make_script
import json


bp = Blueprint("script", __name__, url_prefix="/script")
# ps = ProcessDAO()


@bp.route("/", methods=['GET'])
def index():
   start_range = request.args['start_range']
   print('start_range -> ',start_range)
   end_range = request.args['end_range']
   print('end_range -> ', end_range)
#    make_script(start_range,end_range)
   make_script(start_range, end_range)
   return request.query_string, 200

