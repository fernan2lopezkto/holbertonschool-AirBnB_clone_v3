#!/usr/bin/python3

"""
starts a flask web  app
"""

from os import getenv
from flask import Flask
from api.v1.views import app_views
from models import storage


HBNB_API_HOST = getenv('HBNB_API_HOST')
HBNB_API_PORT = getenv('HBNB_API_PORT')


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def handle_context():
    """Close sotrage"""
    storage.close()

if __name__ == "__main__":
    try:
        app.run(host= HBNB_API_HOST, port= HBNB_API_PORT, threaded=True)
    except:
        app.run(host= '0.0.0.0', port= '5000', threaded= True)

