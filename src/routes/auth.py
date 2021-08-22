from flask import Blueprint
from flask_restful import Api

from resources import RegisterResource
from resources import LoginResource
from resources import LogoutResource

AUTH_BLUEPRINT = Blueprint("auth", __name__)

api = Api(AUTH_BLUEPRINT, prefix="/auth")

api.add_resource(RegisterResource, "/register")
api.add_resource(LoginResource, "/login")
api.add_resource(LogoutResource, "/logout")
