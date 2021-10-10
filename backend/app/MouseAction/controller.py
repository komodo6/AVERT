from flask import Blueprint
import json
from . import MouseActionsDAO

bp = Blueprint('mouseactions', __name__, url_prefix='/mouseactions')

ma = MouseActionsDAO.MouseActionsDAO()

@bp.route('/', methods=['GET'])
def index():
    all_mouseactions = list(ma.read())
    return json.dumps(all_mouseactions)
    
    