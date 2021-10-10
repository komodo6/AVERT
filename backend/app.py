from flask import Flask
from app import create_app


app = create_app()

@app.route('/')
def index():
    return "Hello World"






if __name__ == '__main__':
    # print(test)
    app.run(host="0.0.0.0", port=5000)