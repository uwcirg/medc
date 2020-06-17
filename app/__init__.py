from flask import Flask
from flask_restful import Api

from .medcalc import MEDCalc


def create_app():
    app = Flask(__name__)
    init_app(app)
    return app


def init_app(app):
    api = Api(app)
    api.add_resource(MEDCalc, "/calc")

