from application import app
from application import cache
from application.models import Constituency


@app.route('/constituencies', methods=["GET"])
@cache.cached(timeout=3600)
def constituencies():
    constituencies = Constituency.query.all()
    return repr(constituencies)


@app.route('/constituencies/<id>', methods=["GET"])
@cache.cached(timeout=3600)
def constituency(id):
    pass
