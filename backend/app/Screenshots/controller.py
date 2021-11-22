from bson.json_util import dumps
import re
from flask import Blueprint, send_file, render_template, request
import json
import os
from .CaptureScreenshot import CaptureScreenshot
import bson
from .ScreenshotDAO import ScreemshotDAO
bp = Blueprint('screenshots', __name__, url_prefix='/screenshots')


dao = ScreemshotDAO()

# Getting Screenshots

current_dir = os.path.dirname(os.path.abspath(__file__))


@bp.route('/capture', methods=['GET'])
def screenshot_capture():

    cs = CaptureScreenshot()
    cs.start()
    cs.join()

    return "ok", 200


@bp.route('/images', methods=['GET'])
def get_images():
    images = list(dao.read_all())
    images = json.loads(dumps(images))

    # for image in images:
    #     print(image["ScreenshotSize"])
    # print(list(images))
    return dumps(images), 200


@bp.route('/image', methods=['GET'])
def get_image():
    img = request.args.get("id") if "id" in request.args else None
    if img:
        image = dao.read_id(img)
        image = json.loads(dumps(image))
        image = image[0]
        image = image["ScreenshotFile"]

        img_tag = f'data:image/png;base64,{image}'

        return img_tag, 200
    else:
        return "Image does not exist", 404


@bp.route('/tags', methods=['POST'])
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

@bp.route('/annotations', methods=['POST'])
def update_annotation():
    id = request.get_json()["id"] if "id" in request.get_json() else None
    if id:
        annotation = request.get_json(
        )["annotation"] if "annotation" in request.get_json() else None
        if annotation is not None:
            dao.update_annotation(id, annotation)
            return "Updated", 200
        else:
            return "Missings annotation", 400

    return "Missings id", 400


@bp.route('/image/<id>', methods=['DELETE'])
def delete_image(id):
    img = id
    if img:
        dao.delete(img)
        return img, 200
    else:
        return "Image does not exist", 404
