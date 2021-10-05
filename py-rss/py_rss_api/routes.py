from py_rss_api.app import app
from flask import jsonify


@app.route("/")
def hello_world():
    return jsonify({1: 1})
