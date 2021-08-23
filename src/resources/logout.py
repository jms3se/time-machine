from flask_restful import Resource
from flask_jwt_extended import get_jwt
from flask_jwt_extended import jwt_required
from werkzeug.exceptions import InternalServerError

from repositories import BlocklistRepository

class LogoutResource(Resource):
    @staticmethod
    @jwt_required()
    def post():
        jti = get_jwt()["jti"]

        revoked_token = BlocklistRepository.create(jti=jti)

        if not revoked_token:
            raise InternalServerError("Something went wrong")

        return {'message': 'Logout'}
