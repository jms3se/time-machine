from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from schemas import project_schema
from schemas import projects_schema
from repositories import ProjectRepository
from utils import parse_params

class ProjectsResource(Resource):
    @staticmethod
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

        return project_schema.jsonify(project)

    @staticmethod
    @jwt_required()
    def get():
        projects = ProjectRepository.all()

        result = projects_schema.dump(projects)

        return jsonify(result)
