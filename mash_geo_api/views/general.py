from flask import Response, Blueprint
import json

general_bp = Blueprint('general', __name__)


@general_bp.route("/health")
def check_status():
    return Response(response=json.dumps({
        "status": "OK"
    }), mimetype='application/json', status=200)
