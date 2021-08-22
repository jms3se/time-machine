from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask_jwt_extended import jwt_required

from schemas import tag_schema
from repositories import TagRepository
from utils import parse_params

class TagResource(Resource):
    @staticmethod
    @jwt_required()
    def get(id):
        tag = TagRepository.get(id=id)

        return tag_schema.jsonify(tag)

    @staticmethod
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

        return tag_schema.jsonify(tag)

    @staticmethod
    @jwt_required()
    def delete(id):
        tag = TagRepository.delete(id=id)

        return tag_schema.jsonify(tag)
