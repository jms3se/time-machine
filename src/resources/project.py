from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask_jwt_extended import jwt_required

from schemas import project_schema
from repositories import ProjectRepository
from utils import parse_params

class ProjectResource(Resource):
    @staticmethod
    @jwt_required()
    def get(id):
        tag = ProjectRepository.get(id=id)

        return project_schema.jsonify(tag)

    @staticmethod
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

        return project_schema.jsonify(project)

    @staticmethod
    @jwt_required()
    def delete(id):
        project = ProjectRepository.delete(id=id)

        return project_schema.jsonify(project)
