from flask import Flask
from flask_socketio import SocketIO
import pymongo

client = pymongo.MongoClient(host="54.164.164.164", port=27017)

db = client.AVERT

socketio = SocketIO()


def create_app():
    app = Flask(__name__)

    # for websockets
    socketio.init_app(app)

    from app.Keystroke.controller import bp as keystrokes
    from app.MouseAction.controller import bp as MouseActions
    from app.Recorder.controller import bp as recorder
    from app.Screenshots.controller import bp as screenshots
    from app.Process.controller import bp as process
    from app.SystemCalls.controller import bp as systemcall
    from app.Video.Controller import bp as videos
    from app.Scripts.controller import bp as scripting
    from app.WindowHistory.controller import bp as windowhistory
    from app.PacketCapture.controller import bp as networkdata
    from app.Sync.controller import bp as sync

    app.register_blueprint(keystrokes)
    app.register_blueprint(MouseActions)
    app.register_blueprint(screenshots)
    app.register_blueprint(recorder)
    app.register_blueprint(process)
    app.register_blueprint(systemcall)
    app.register_blueprint(videos)
    app.register_blueprint(scripting)
    app.register_blueprint(windowhistory)
    app.register_blueprint(networkdata)
    app.register_blueprint(sync)

    return app
