from application import app
from application import cache
from flask import request


@app.route('/constituencies', methods=["GET"])
@cache.cached(timeout=3600)
def constituencies():
    pass


@app.route('/constituencies/<id>', methods=["GET"])
@cache.cached(timeout=3600)
def constituency(id):
    pass
