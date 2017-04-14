from flask import Response, Blueprint, request
from mash_place_api import limiter
from flask_negotiate import produces
import json

general_bp = Blueprint('general', __name__)


@general_bp.route("/health", methods=['GET'])
@produces('application/json')
@limiter.exempt
def healthcheck():
    return Response(response=json.dumps({
        "status": "OK"
    }, separators=(',', ':')), mimetype='application/json', status=200)


@general_bp.route("/", methods=["GET"])
@produces('application/json')
def catalogue():
    return Response(response=json.dumps({
        "routes": [{"url": request.url + "boundaries",
                    "description": "Boundaries"}]
    }, separators=(',', ':')), mimetype='application/json', status=200)
