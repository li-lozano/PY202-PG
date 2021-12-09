import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    from . import pg
    app.register_blueprint(pg.bp)
    return app