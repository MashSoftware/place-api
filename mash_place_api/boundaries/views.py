from flask import Response, Blueprint
from mash_place_api import cache
from mash_place_api.models import Constituency, County
import json

boundaries_bp = Blueprint('boundaries', __name__)

routes = [{"url": "/counties",
           "methods": ["GET"],
           "description": "Counties"},
          {"url": "/constituencies",
           "methods": ["GET"],
           "description": "Westminster Constituencies"}]


@boundaries_bp.route('/', methods=['GET'])
def get_boundaries():
    return Response(json.dumps({
        "routes": routes
    }, separators=(',', ':')), mimetype='application/json', status=200)


@boundaries_bp.route('/constituencies', methods=['GET'])
@cache.cached(timeout=86400)
def get_constituencies():
    constituencies = Constituency.query.order_by(Constituency.name).all()
    results = []
    for constituency in constituencies:
        item = constituency.get_keyval()
        results.append(item)
    return Response(json.dumps(results, separators=(',', ':')),
                    mimetype='application/json',
                    status=200)


@boundaries_bp.route('/constituencies/<string:ons_code>', methods=['GET'])
@cache.memoize(timeout=86400)
def get_constituency(ons_code):
    constituency = Constituency.query.get_or_404(ons_code)
    return Response(constituency.get_geojson(),
                    mimetype='application/json',
                    status=200)


@boundaries_bp.route('/counties', methods=['GET'])
@cache.cached(timeout=86400)
def get_counties():
    counties = County.query.order_by(County.name).all()
    results = []
    for county in counties:
        item = county.get_keyval()
        results.append(item)
    return Response(json.dumps(results, separators=(',', ':')),
                    mimetype='application/json',
                    status=200)


@boundaries_bp.route('/counties/<string:ons_code>', methods=['GET'])
@cache.memoize(timeout=86400)
def get_county(ons_code):
    county = County.query.get_or_404(ons_code)
    return Response(county.get_geojson(),
                    mimetype='application/json',
                    status=200)
