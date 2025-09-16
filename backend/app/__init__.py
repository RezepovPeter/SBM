from flask import Flask
from .api.resources import resources
from .extensions import db


def create_app():

    app = Flask(__name__)

    #db.init_app(app)

    app.register_blueprint(resources, url_prefix='/api/resources')

    return app