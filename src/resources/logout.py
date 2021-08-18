from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required

from schemas import user_schema
from repositories import BlocklistRepository

class LogoutResource(Resource):
    @staticmethod
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]

        revoked_token = BlocklistRepository.create(jti=jti)

        if not revoked_token:
            return {'message': 'Something went wrong'}, 500

        return {'message': 'Logout'}
