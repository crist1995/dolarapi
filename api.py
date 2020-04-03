#!flask/bin/python
from flask import Flask, jsonify
import app
apps = Flask(__name__)

@apps.route('/')
def index():
    return str(app.value()).split("'")[1]

if __name__ == '__main__':
    apps.run(host='0.0.0.0', port=80)
