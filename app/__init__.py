from flask import Flask
from flask.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    with app.app_context():
        from .import routes

    return app


    