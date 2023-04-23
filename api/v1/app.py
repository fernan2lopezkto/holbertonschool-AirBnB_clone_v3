#!/usr/bin/python3
"""
This is a Flask application that runs an API with a blueprint for views and closes a storage context
when the application context is torn down.
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
    """
    This function closes a storage context.
    """
    storage.close()


# This code block is checking if the current module is being run as the main program (as opposed to
# being imported as a module into another program). If it is being run as the main program, it tries
# to run the Flask application with the specified host and port, and with threading enabled. If an
# exception occurs (such as if the specified host and port are not available), it runs the Flask
# application with a default host and port.
if __name__ == "__main__":
    try:
        app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
    except:
        app.run(host='0.0.0.0', port='5000', threaded=True)
