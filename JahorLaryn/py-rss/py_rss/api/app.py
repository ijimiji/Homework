from flask import Flask
from flask import request
from werkzeug.exceptions import abort
from cli import RSSReader
from datetime import datetime

app = Flask(__name__)


@app.route("/news/")
def get():
    limit = request.args.get("limit")
    if not limit is None:
        limit = int(limit)
    source = request.args.get("source")
    if source is None:
        abort(400)

    time = datetime.now().strftime("%Y%d%m")
    settings = {"limit": limit, "date": time, "verbose": False, "json": False}

    rss = RSSReader(source, settings)
    return rss.as_json()
