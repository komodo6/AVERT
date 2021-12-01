from flask import Blueprint, request, send_file
from .PacketCapture import PacketCapture
import os
from .PacketCaptureDAO import PacketCaptureDAO
import json
from .PacketCaptureService import PacketCaptureService
bp = Blueprint("PacketCapture", __name__, url_prefix="/networkdata")
from bson.json_util import dumps


dao = PacketCaptureDAO()

packetCaptureOFF = True


@bp.route("/")
def getPCAPFIles():
    return dumps(dao.getAllPCAPS())



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
    global pc, packetCaptureOFF
    if packetCaptureOFF:
        packetCaptureOFF = False
        pc = PacketCapture(interface_name="eth0")
        pc.start()
        return " Started Packet Capture", 200
    else:
        pc.stop()
        return " Stopped Packet Capture", 200



@bp.route("/stop")
def stopPacketCapture():
    pc.stop()
    pc.join()
    return "Stopped Network Capture"

@bp.route("/health")
def health_check():
    return "ok", 200

@bp.route('/count', methods=['GET'])
def get_count_packets():
    try:
        count = dao.get_count()
        print(count)
        return json.dumps(count)
        # return list(ks.read())
    except Exception as e:
        print(e)
        return 'error'    
    