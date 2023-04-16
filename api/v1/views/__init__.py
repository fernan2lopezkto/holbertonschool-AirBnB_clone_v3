#!/usr/bin/python3
""" module to create app views for blueprint"""

from flask import Blueprint
from api.v1.views.index import app_views


app_views = Blueprint(url_prefix='/api/v1')
