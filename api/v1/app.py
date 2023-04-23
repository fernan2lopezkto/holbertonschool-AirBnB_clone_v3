#!/usr/bin/python3
"""
This is a Flask application that runs an API with a blueprint for views and closes a storage context
when the application context is torn down.
"""

# imports
from flask import Flask
from models import storage
from os import getenv
from api.v1.views import app_views
"""instancies my app"""
app = Flask(__name__)

"""register blueprint template in my appi"""
app.register_blueprint(app_views)


@app.teardown_appcontext
def handle_cont(exeption):
    """This function closes a storage context."""
    storage.close()

if __name__ == '__main__':
    """run my app"""
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)