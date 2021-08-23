from flask_restful import Resource
from flask_restful import marshal_with
from flask_jwt_extended import jwt_required

from repositories import TimerProjectRepository
from schemas import timer_fields

class TimerProjectResource(Resource):
    @staticmethod
    @marshal_with(timer_fields)
    @jwt_required()
    def delete(id, project_id):
        timer = TimerProjectRepository.delete(id=id, project_id=project_id)

        return timer
