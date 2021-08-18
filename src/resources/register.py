from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from schemas import user_schema
from repositories import UserRepository
from utils import generate_hash
from utils import check_hash
from utils import parse_params

class RegisterResource(Resource):
    @staticmethod
    @parse_params(
        Argument("name", location="json", required=True, help="Name is required"),
        Argument("email", location="json", required=True, help="Email is required"),
        Argument("password", location="json", required=True, help="Password is required")
    )
    def post(name, email, password):
        user = UserRepository.create(
            name=name, email=email, password=password
        )

        return user_schema.jsonify(user)
