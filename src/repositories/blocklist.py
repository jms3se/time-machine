from flask import jsonify

from . import get_redis_connection

class BlocklistRepository:
    @staticmethod
    def create(jti):
        get_redis_connection().set(jti, "")

        return jsonify({"message": "access token revoked"})

    @staticmethod
    def get(jti):
        return get_redis_connection().get(jti)
