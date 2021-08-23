from flask_restful import Resource
from flask_restful import marshal_with
from flask_jwt_extended import jwt_required
from flask_restful.reqparse import Argument

from repositories import TimerProjectRepository
from schemas import project_list_fields
from utils import parse_params

class TimerProjectsResource(Resource):
    @staticmethod
    @parse_params(
        Argument("project_id", location="json", required=True, help="ProjectId is required")
    )
    @jwt_required()
    def post(id, project_id):
        timer = TimerProjectRepository.create(
            id=id,
            project_id=project_id
        )

        return timer

    @staticmethod
    @marshal_with(project_list_fields)
    @jwt_required()
    def get(id):
        timer_projects = TimerProjectRepository.get(id=id)

        return { "items": timer_projects }
