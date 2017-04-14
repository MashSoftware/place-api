from mash_place_api import app
from flask import Response
import json


@app.errorhandler(404)
def not_found(error):
    return Response(response=json.dumps({"status_code": "404",
                                         "message": "Not Found"}, separators=(',', ':')),
                    mimetype='application/json',
                    status=404)


@app.errorhandler(405)
def method_not_allowed(error):
    return Response(response=json.dumps({"status_code": "405",
                                         "message": "Method Not Allowed"}, separators=(',', ':')),
                    mimetype='application/json',
                    status=405)


@app.errorhandler(406)
def not_acceptable(error):
    return Response(response=json.dumps({"status_code": "406",
                                         "message": "Not Accetpable"}, separators=(',', ':')),
                    mimetype='application/json',
                    status=406)


@app.errorhandler(429)
def too_many_requests(error):
    return Response(response=json.dumps({"status_code": "429",
                                         "message": "Too Many Requests"}, separators=(',', ':')),
                    mimetype='application/json',
                    status=429)


@app.errorhandler(500)
def internal_server_error(error):
    return Response(response=json.dumps({"status_code": "500",
                                         "message": "Internal Server Error"}, separators=(',', ':')),
                    mimetype='application/json',
                    status=500)
