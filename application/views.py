from application import app
from application.models import Constituency


@app.route('/constituencies', methods=["GET"])
def constituencies():
    constituencies = Constituency.query.all()
    return repr(constituencies)


@app.route('/constituencies/<id>', methods=["GET"])
def constituency(id):
    constituency = Constituency.query.get(id)
    return repr(constituency)
