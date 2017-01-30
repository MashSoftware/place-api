from flask import Response, Blueprint, request
from mash_place_api import limiter
import json

general_bp = Blueprint('general', __name__)


@general_bp.route("/health", methods=['GET'])
@limiter.exempt
def healthcheck():
    return Response(response=json.dumps({
        "status": "OK"
    }, separators=(',', ':')), mimetype='application/json', status=200)


@general_bp.route("/", methods=["GET"])
def catalogue():
    return Response(response=json.dumps({
        "routes": [{"url": request.url + "boundaries",
                    "description": "Boundaries"}]
    }, separators=(',', ':')), mimetype='application/json', status=200)
