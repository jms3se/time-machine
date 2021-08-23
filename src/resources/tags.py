from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful.reqparse import Argument
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from schemas import tag_fields
from schemas import tag_list_fields
from repositories import TagRepository
from utils import parse_params

class TagsResource(Resource):
    @staticmethod
    @marshal_with(tag_fields)
    @parse_params(
        Argument("name", location="json", required=True, help="Name is required"),
        Argument("description", location="json", required=False),
    )
    @jwt_required()
    def post(name, description):
        user_id = get_jwt_identity()['id']

        tag = TagRepository.create(
            user_id=user_id,
            name=name,
            description=description
        )

        return tag

    @staticmethod
    @marshal_with(tag_list_fields)
    @jwt_required()
    def get():
        tags = TagRepository.all()

        return { "items": tags }
