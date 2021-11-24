from flask import Blueprint, request, send_file
from .PacketCapture import PacketCapture
import os
from .PacketCaptureDAO import PacketCaptureDAO
import json
from .PacketCaptureService import PacketCaptureService
bp = Blueprint("PacketCapture", __name__, url_prefix="/networkdata")
from bson.json_util import dumps
pc = PacketCapture(interface_name="eth0")

dao = PacketCaptureDAO()


@bp.route("/")
def getPCAPFIles():
    return dumps(dao.getAllPCAPS())

@bp.route("/t")
def vid():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, "./Output.mp4")
    return send_file(path)

@bp.route("/pcap")
def getPCAPData():
    if "filename" in request.args:
        filename = request.args.get("filename")
        pcs = PacketCaptureService(filename)
        data = pcs.getPCAPPackets(filename)
        return dumps(data)
        # return dumps(dao.getAllPCAPS())
    else:
        return "Missing filename"

@bp.route("/start")
def startPacketCapture():
    global pc
    print(pc.is_alive())
    if pc.is_alive():
        pc.stop()
        pc.join()
    else:
        pc.setDaemon(True)
        pc.start()
        
    
    return "Started Network Capture"


@bp.route("/stop")
def stopPacketCapture():
    pc.stop()
    pc.join()
    return "Stopped Network Capture"

@bp.route("/health")
def health_check():
    return "ok", 200
    