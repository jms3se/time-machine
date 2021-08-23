from flask import jsonify
from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful.reqparse import Argument
from flask_jwt_extended import create_access_token
from werkzeug.exceptions import Unauthorized

from schemas import user_login_fields
from repositories import UserRepository
from utils import parse_params

class LoginResource(Resource):
    @staticmethod
    @marshal_with(user_login_fields)
    @parse_params(
        Argument("email", location="json", required=True, help="Email is required"),
        Argument("password", location="json", required=True, help="Password is required")
    )
    def post(email, password):
        user = UserRepository.getByEmail(email)

        if not user:
            raise Unauthorized("User not found")

        isOk = user.verify_password(password)

        if not isOk:
            raise Unauthorized("User not found")

        access_token = create_access_token(identity = {"id": user.id})

        user.access_token = access_token

        return user
