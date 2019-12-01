from flask import Flask
from main import *
app = Flask(__name__)

@app.route("/<username>", methods=['GET_FREE'])
def index(username):

    return get_json(1)

@app.route("/<username>", methods=['GET_BISY'])
def index(username):

    return get_json(0)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
