from mash_place_api import app
from flask import Response
import json


@app.errorhandler(404)
def not_found(error):
    return Response(response=json.dumps({"status_code": "404",
                                         "message": "Not Found"}),
                    mimetype='application/json',
                    status=404)


@app.errorhandler(405)
def method_not_allowed(error):
    return Response(response=json.dumps({"status_code": "405",
                                         "message": "Method Not Allowed"}),
                    mimetype='application/json',
                    status=405)
