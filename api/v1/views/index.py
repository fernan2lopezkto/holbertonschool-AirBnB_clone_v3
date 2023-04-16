#!/usr/bin/python3
"""This module provides a simple get status of the web server."""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def ret_status():
    status = {"status": "OK"}
    return jsonify(status)
