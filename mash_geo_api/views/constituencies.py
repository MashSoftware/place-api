from flask import Response, Blueprint
from mash_geo_api import cache
from mash_geo_api.models import Constituency

constituencies_bp = Blueprint('constituencies', __name__)


@constituencies_bp.route('/', methods=['GET'])
@cache.cached(timeout=86400)
def constituencies():
    constituencies = Constituency.query.all()
    return Response(repr(constituencies),
                    mimetype='application/json',
                    status=200)


@constituencies_bp.route('/<ons_code>', methods=['GET'])
@cache.memoize(timeout=86400)
def constituency(ons_code):
    constituency = Constituency.query.get_or_404(ons_code)
    return Response(repr(constituency), mimetype='application/json', status=200)
