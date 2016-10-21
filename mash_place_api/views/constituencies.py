from flask import Response, Blueprint
from mash_place_api import cache
from mash_place_api.models import Constituency
import json

constituencies_bp = Blueprint('constituencies', __name__)


@constituencies_bp.route('/', methods=['GET'])
@cache.cached(timeout=86400)
def get_constituencies():
    constituencies = Constituency.query.order_by(Constituency.name).all()
    results = []
    for constituency in constituencies:
        item = constituency.get_properties()
        results.append(item)
    return Response(json.dumps(results), mimetype='application/json', status=200)


@constituencies_bp.route('/<string:ons_code>', methods=['GET'])
@cache.memoize(timeout=86400)
def get_constituency(ons_code):
    constituency = Constituency.query.get_or_404(ons_code)
    return Response(constituency.get_geojson(), mimetype='application/json', status=200)
