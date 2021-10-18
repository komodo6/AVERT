from flask import Flask

import pymongo


client = pymongo.MongoClient(host="localhost", port=27017)

db = client.AVERT



def create_app():
    app = Flask(__name__)

    from app.Keystroke.controller import bp as keystrokes
    from app.MouseAction.controller import bp as MouseActions
    from app.Screenshots.controller import bp as screenshots

    app.register_blueprint(keystrokes)
    app.register_blueprint(MouseActions)
    app.register_blueprint(screenshots)


    return app