import re
from flask import Blueprint, send_file, render_template, request
import json
import os
from .Services.CaptureScreenshot import CaptureScreenshot

from .ScreenshotDAO import ScreemshotDAO
bp = Blueprint('screenshots', __name__, url_prefix='/screenshots')

dao = ScreemshotDAO()

# Getting Screenshots

current_dir = os.path.dirname(os.path.abspath(__file__))

@bp.route('/capture', methods=['GET'])
def screenshot_capture():
    
    cs = CaptureScreenshot()
    print(cs.start())
    cs.join()

    
   
   

    return "ok", 200     



@bp.route('/images', methods=['GET'])
def get_images():
    images = list(dao.read())

    return json.dumps(images), 200
    

@bp.route('/image', methods=['GET'])
def get_image():
    img = request.args.get("id") if "id" in request.args else None
    if img:
        image = list(dao.read(img))
        
        img_id = image[0]['image_id']

        return send_file(os.path.join( current_dir,f"../images/{img_id}.png"), mimetype="image/png"), 200
    else:
        return "Image does not exist", 404
    


