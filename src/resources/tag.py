from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful.reqparse import Argument
from flask_jwt_extended import jwt_required

from schemas import tag_fields
from repositories import TagRepository
from utils import parse_params

class TagResource(Resource):
    @staticmethod
    @marshal_with(tag_fields)
    @jwt_required()
    def get(id):
        tag = TagRepository.get(id=id)

        return tag

    @staticmethod
    @marshal_with(tag_fields)
    @parse_params(
        Argument("name", location="json", required=True, help="Name is required"),
        Argument("description", location="json", required=False),
    )
    @jwt_required()
    def put(id, name, description):
        tag = TagRepository.update(
            id=id,
            name=name,
            description=description
        )

        return tag

    @staticmethod
    @marshal_with(tag_fields)
    @jwt_required()
    def delete(id):
        tag = TagRepository.delete(id=id)

        return tag
