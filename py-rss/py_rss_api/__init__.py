from flask import Flask, jsonify
from .. import py_rss_cli

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({1: 1})


if __name__ == "__main__":
    app.run()
