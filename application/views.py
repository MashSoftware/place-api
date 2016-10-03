from flask import Response
from application import app
from application.models import Constituency


@app.route('/constituencies', methods=["GET"])
def constituencies():
    constituencies = Constituency.query.all()
    return Response(repr(constituencies), mimetype='application/json')


@app.route('/constituencies/<id>', methods=["GET"])
def constituency(id):
    constituency = Constituency.query.get(id)
    return Response(repr(constituency), mimetype='application/json')
