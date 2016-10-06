from flask import Response, Blueprint, request
from mash_geo_api import app, cache
from mash_geo_api.models import Constituency

constituencies_bp = Blueprint('constituencies', __name__)


@constituencies_bp.route('/', methods=["GET"])
@cache.cached(timeout=86400)
def constituencies():
    app.logger.info('GET ' + request.url)
    constituencies = Constituency.query.all()
    return Response(repr(constituencies), mimetype='application/json')


@constituencies_bp.route('/<id>', methods=["GET"])
@cache.memoize(timeout=86400)
def constituency(id):
    app.logger.info('GET ' + request.url)
    constituency = Constituency.query.get(id)
    return Response(repr(constituency), mimetype='application/json')
