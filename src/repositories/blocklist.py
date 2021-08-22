from flask import jsonify

from src.database import get_redis_connection

class BlocklistRepository:
    @staticmethod
    def create(jti):
        redis = get_redis_connection()

        redis.set(jti, "")

        return jsonify({"message": "access token revoked"})

    @staticmethod
    def get(jti):
        redis = get_redis_connection()

        result = redis.get(jti)

        return result
