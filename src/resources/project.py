from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful.reqparse import Argument
from flask_jwt_extended import jwt_required

from schemas import project_fields
from repositories import ProjectRepository
from utils import parse_params

class ProjectResource(Resource):
    @staticmethod
    @marshal_with(project_fields)
    @jwt_required()
    def get(id):
        project = ProjectRepository.get(id=id)

        return project

    @staticmethod
    @marshal_with(project_fields)
    @parse_params(
        Argument("name", location="json", required=True, help="Name is required"),
        Argument("description", location="json", required=False),
    )
    @jwt_required()
    def put(id, name, description):
        project = ProjectRepository.update(
            id=id,
            name=name,
            description=description
        )

        return project

    @staticmethod
    @marshal_with(project_fields)
    @jwt_required()
    def delete(id):
        project = ProjectRepository.delete(id=id)

        return project
