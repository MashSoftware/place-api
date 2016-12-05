from flask import Response, Blueprint, request
from mash_place_api import cache
from mash_place_api.models import WestminsterConstituency, County, LondonAssemblyConstituency
import json

boundaries_bp = Blueprint('boundaries', __name__)


@boundaries_bp.route('/', methods=['GET'])
def get_boundaries():
    return Response(json.dumps({
        "routes": [{"url": request.url + "counties",
                   "description": "County"},
                   {"url": request.url + "constituencies",
                   "description": "Westminster Constituency"},
                   {"url": request.url + "londonassemblies",
                   "description": "Greater London Authority Assembly Constituency"}]
    }, separators=(',', ':')), mimetype='application/json', status=200)


@boundaries_bp.route('/constituencies', methods=['GET'])
@cache.cached(timeout=86400)
def get_constituencies():
    constituencies = WestminsterConstituency.query.order_by(WestminsterConstituency.name).all()
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
    constituency = WestminsterConstituency.query.get_or_404(ons_code)
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


@boundaries_bp.route('/londonassemblies', methods=['GET'])
@cache.cached(timeout=86400)
def get_londons():
    londons = LondonAssemblyConstituency.query.order_by(LondonAssemblyConstituency.name).all()
    results = []
    for london in londons:
        item = london.get_keyval()
        results.append(item)
    return Response(json.dumps(results, separators=(',', ':')),
                    mimetype='application/json',
                    status=200)


@boundaries_bp.route('/londonassemblies/<string:ons_code>', methods=['GET'])
@cache.memoize(timeout=86400)
def get_london(ons_code):
    london = LondonAssemblyConstituency.query.get_or_404(ons_code)
    return Response(london.get_geojson(),
                    mimetype='application/json',
                    status=200)
