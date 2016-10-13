from flask import Response, Blueprint
from mash_geo_api import cache
from mash_geo_api.models import Constituency

constituencies_bp = Blueprint('constituencies', __name__)


@constituencies_bp.route('/', methods=["GET"])
@cache.cached(timeout=86400)
def constituencies():
    constituencies = Constituency.query.all()
    return Response(repr(constituencies), mimetype='application/json', status=200)


@constituencies_bp.route('/<id>', methods=["GET"])
@cache.memoize(timeout=86400)
def constituency(id):
    constituency = Constituency.query.get(id)
    return Response(repr(constituency), mimetype='application/json', status=200)
