from flask import Blueprint
from flask_restful import Api

from resources import LogoutResource

LOGOUT_BLUEPRINT = Blueprint("logout", __name__)
Api(LOGOUT_BLUEPRINT).add_resource(
    LogoutResource, "/logout"
)
