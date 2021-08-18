from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask_jwt_extended import create_access_token

from schemas import user_schema
from repositories import UserRepository
from utils import generate_hash
from utils import check_hash
from utils import parse_params

class LoginResource(Resource):
    @staticmethod
    @parse_params(
        Argument("email", location="json", required=True, help="Email is required"),
        Argument("password", location="json", required=True, help="Password is required")
    )
    def post(email, password):
        user = UserRepository.getByEmail(email)

        if not user:
            return {"message": "user not found"}, 403

        isOk = user.verify_password(password)

        if not isOk:
            return {"message": "user not found"}, 403

        access_token = create_access_token(identity = {"id": user.id})

        user_json = user_schema.dump(user)

        return jsonify({
            "user": user_json,
            "access_token": access_token
        })
