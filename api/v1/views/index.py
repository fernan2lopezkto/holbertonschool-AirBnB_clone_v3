#!/usr/bin/python3
""" documentation """

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def ret_status():
    status = {"status": "OK"}
    return jsonify(status)
