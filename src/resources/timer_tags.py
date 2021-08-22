from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask_restful.reqparse import Argument

from repositories import TimerTagRepository
from schemas import tags_schema
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
    @jwt_required()
    def get(id):
        timer_tags = TimerTagRepository.get(id=id)

        result = tags_schema.dump(timer_tags)

        return jsonify(result)
