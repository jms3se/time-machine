from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful.reqparse import Argument

from schemas import user_fields
from repositories import UserRepository
from utils import parse_params

class RegisterResource(Resource):
    @staticmethod
    @marshal_with(user_fields)
    @parse_params(
        Argument("name", location="json", required=True, help="Name is required"),
        Argument("email", location="json", required=True, help="Email is required"),
        Argument("password", location="json", required=True, help="Password is required")
    )
    def post(name, email, password):
        user = UserRepository.create(
            name=name, email=email, password=password
        )

        return user
