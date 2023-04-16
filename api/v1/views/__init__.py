#!/usr/bin/python3
""" documentation """

from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint(url_prefix='/api/v1')
