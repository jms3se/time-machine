from flask_restful import Resource
from flask_restful import marshal_with
from flask_jwt_extended import jwt_required
from flask_restful.reqparse import Argument

from repositories import TimerTagRepository
from schemas import tag_list_fields
from utils import parse_params

class TimerTagsResource(Resource):
    @staticmethod
    @parse_params(
        Argument("tag_id", location="json", required=True, help="TagId is required")
    )
    @jwt_required()
    def post(id, tag_id):
        timer = TimerTagRepository.create(
            id=id,
            tag_id=tag_id
        )

        return timer

    @staticmethod
    @marshal_with(tag_list_fields)
    @jwt_required()
    def get(id):
        timer_tags = TimerTagRepository.get(id=id)

        return { "items": timer_tags }
