from flask import Blueprint
from flask_restful import Api

from resources import ProjectResource
from resources import ProjectsResource

PROJECT_BLUEPRINT = Blueprint("project", __name__)

api = Api(PROJECT_BLUEPRINT)

api.add_resource(ProjectsResource, "/projects")
api.add_resource(ProjectResource, "/projects/<int:id>")
