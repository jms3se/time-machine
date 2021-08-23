from flask_restful import Resource
from flask_restful import marshal_with
from flask_jwt_extended import jwt_required

from repositories import TimerTagRepository
from schemas import timer_fields

class TimerTagResource(Resource):
    @staticmethod
    @marshal_with(timer_fields)
    @jwt_required()
    def delete(id, tag_id):
        timer = TimerTagRepository.delete(id=id, tag_id=tag_id)

        return timer
