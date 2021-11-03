from flask import Flask

import pymongo

client = pymongo.MongoClient(host="54.215.46.201", port=27017)

db = client.AVERT


def create_app():
    app = Flask(__name__)

    from app.Keystroke.controller import bp as keystrokes
    from app.MouseAction.controller import bp as MouseActions
    from app.Recorder.controller import bp as recorder
    from app.Screenshots.controller import bp as screenshots
    from app.Process.controller import bp as process
    from app.SystemCalls.controller import bp as systemcall
    from app.Video.Controller import bp as videos
    from app.Scripts.controller import bp as scripting
    from app.WindowHistory.controller import bp as windowhistory

    app.register_blueprint(keystrokes)
    app.register_blueprint(MouseActions)
    app.register_blueprint(screenshots)
    app.register_blueprint(recorder)
    app.register_blueprint(process)
    app.register_blueprint(systemcall)
    app.register_blueprint(videos)
    app.register_blueprint(scripting)
    app.register_blueprint(windowhistory)

    return app
