from flask import Blueprint
from flask_restful import Api

from resources import RegisterResource

REGISTER_BLUEPRINT = Blueprint("register", __name__)
Api(REGISTER_BLUEPRINT).add_resource(
    RegisterResource, "/register"
)
