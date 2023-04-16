#!/usr/bin/python3
""" documentation  jkghjsf sghsg  shthst"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def ret_status():
    """la documentacion"""
    status = {"status": "OK"}
    return jsonify(status)
