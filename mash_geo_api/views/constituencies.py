from flask import Response, Blueprint
from mash_geo_api import cache
from mash_geo_api.models import Constituency
import json

constituencies_bp = Blueprint('constituencies', __name__)


@constituencies_bp.route('/', methods=['GET'])
@cache.cached(timeout=86400)
def constituencies():
    constituencies = Constituency.query.all()
    results = []
    for constituency in constituencies:
        item = constituency.get_properties()
        results.append(item)
    return Response(json.dumps(results), mimetype='application/json', status=200)


@constituencies_bp.route('/<ons_code>', methods=['GET'])
@cache.memoize(timeout=86400)
def constituency(ons_code):
    constituency = Constituency.query.get_or_404(ons_code)
    return Response(constituency.get_geojson(), mimetype='application/json', status=200)
