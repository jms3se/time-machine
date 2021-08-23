from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful.reqparse import Argument
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from schemas import project_fields
from schemas import project_list_fields
from repositories import ProjectRepository
from utils import parse_params

class ProjectsResource(Resource):
    @staticmethod
    @marshal_with(project_fields)
    @parse_params(
        Argument("name", location="json", required=True, help="Name is required"),
        Argument("description", location="json", required=False),
    )
    @jwt_required()
    def post(name, description):
        user_id = get_jwt_identity()['id']

        project = ProjectRepository.create(
            user_id=user_id,
            name=name,
            description=description
        )

        return project

    @staticmethod
    @marshal_with(project_list_fields)
    @jwt_required()
    def get():
        projects = ProjectRepository.all()

        return { "items": projects }
