from flask import Response, Blueprint
from mash_place_api import cache
from mash_place_api.models import County
import json

counties_bp = Blueprint('counties', __name__)


@counties_bp.route('/', methods=['GET'])
@cache.cached(timeout=86400)
def get_counties():
    counties = County.query.order_by(County.name).all()
    results = []
    for county in counties:
        item = county.get_keyval()
        results.append(item)
    return Response(json.dumps(results), mimetype='application/json', status=200)


@counties_bp.route('/<string:ons_code>', methods=['GET'])
@cache.memoize(timeout=86400)
def get_county(ons_code):
    county = County.query.get_or_404(ons_code)
    return Response(county.get_geojson(), mimetype='application/json', status=200)
