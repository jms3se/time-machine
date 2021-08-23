from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful.reqparse import Argument
from flask_jwt_extended import jwt_required

from schemas import timer_fields
from repositories import TimerRepository
from utils import parse_params

class TimerResource(Resource):
    @staticmethod
    @marshal_with(timer_fields)
    @jwt_required()
    def get(id):
        timer = TimerRepository.get(id=id)

        return timer

    @staticmethod
    @marshal_with(timer_fields)
    @parse_params(
        Argument("name", location="json", required=True, help="Name is required"),
        Argument("start", location="json", required=True, help="Start is required"),
        Argument("description", location="json", required=False),
        Argument("stop", location="json", required=False)
    )
    @jwt_required()
    def put(id, name, start, description, stop):
        timer = TimerRepository.update(
            id=id,
            name=name,
            start=start,
            description=description,
            stop=stop
        )

        return timer

    @staticmethod
    @marshal_with(timer_fields)
    @jwt_required()
    def delete(id):
        timer = TimerRepository.delete(id=id)

        return timer
