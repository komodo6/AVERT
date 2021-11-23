from flask import Flask
from app import create_app, socketio
from flask_cors import CORS



app = create_app()

CORS(app)


@app.route('/')
def index():
    return "Hello World"


if __name__ == '__main__':
    # print(test)
    socketio.run(app, host="0.0.0.0", port=5000)
