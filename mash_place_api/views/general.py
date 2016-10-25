from flask import Response, Blueprint, request
import json

general_bp = Blueprint('general', __name__)

routes = [{"url": "/constituencies",
           "methods": ["GET"],
           "description": "List of Westminster Constituencies",
           "collection": "Boundaries"},
          {"url": "/constituencies/<string:ons_code>",
           "methods": ["GET"],
           "description": "Westminster Constituency",
           "collection": "Boundaries"},
          {"url": "/counties",
           "methods": ["GET"],
           "description": "List of Counties",
           "collection": "Boundaries"},
          {"url": "/counties/<string:ons_code>",
           "methods": ["GET"],
           "description": "County",
           "collection": "Boundaries"}]


@general_bp.route("/health", methods=['GET'])
def healthcheck():
    return Response(response=json.dumps({
        "status": "OK"
    }), mimetype='application/json', status=200)


@general_bp.route("/", methods=["GET"])
def catalogue():
    return Response(response=json.dumps({
        "base_url": request.url_root[:-1],
        "routes": routes
    }), mimetype='application/json', status=200)
