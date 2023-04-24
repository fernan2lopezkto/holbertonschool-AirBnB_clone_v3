#!/usr/bin/python3
""" module to create app views for blueprint"""

from flask import Blueprint

# app_views = Blueprint(url_prefix='/api/v1')
"""I define my blueprint model"""
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *