#!/usr/bin/python3
"""http methods for manipulating sate class resources"""

from api.v1.views import app_views

from models.state import State
from models import storage

from flask import jsonify

@app_views.route('/states', strict_slashes=False)
def get_states():
    """Return a list of all states"""
    states = storage.all(State).values()
    state_list = [state.to_dict() for state in states]
    return jsonify(state_list)