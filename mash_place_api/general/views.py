from flask import Response, Blueprint
import json

general_bp = Blueprint('general', __name__)

routes = [{"url": "/boundaries",
           "methods": ["GET"],
           "description": "Administrative areas in England, Scotland and Wales."}]


@general_bp.route("/health", methods=['GET'])
def healthcheck():
    return Response(response=json.dumps({
        "status": "OK"
    }, separators=(',', ':')), mimetype='application/json', status=200)


@general_bp.route("/", methods=["GET"])
def catalogue():
    return Response(response=json.dumps({
        "routes": routes
    }, separators=(',', ':')), mimetype='application/json', status=200)
