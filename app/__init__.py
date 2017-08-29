""" this module deals with the creation of the application"""

from flask import Flask

from config import app_config
from models import Storage

store = Storage()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    from .landing_page import landing_page as landing_page_blueprint
    app.register_blueprint(landing_page_blueprint)

    return app
