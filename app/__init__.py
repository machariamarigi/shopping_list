""" this module deals with the creation of the application"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from config import app_config
from .models import Storage

store = Storage()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    Bootstrap(app)

    from .landing_page import landing_page as landing_page_blueprint
    app.register_blueprint(landing_page_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    @app.errorhandler(404)
    def page_not_found(error):
        """Method to handle 404 errors"""
        return render_template('404.html', title='Page Not Found'), 404

    @app.errorhandler(401)
    def unauthorized(error):
        """Method to handle 401 errors"""
        return render_template('401.html', title='Unauthorized'), 401

    @app.errorhandler(500)
    def internal_server_error(error):
        """Method to handle 400 errors"""
        return render_template('500.html', title='Server error'), 500

    return app
