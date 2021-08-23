from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful.reqparse import Argument
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from schemas import timer_fields
from schemas import timer_list_fields
from repositories import TimerRepository
from utils import parse_params

class TimersResource(Resource):
    @staticmethod
    @marshal_with(timer_fields)
    @parse_params(
        Argument("name", location="json", required=True, help="Name is required"),
        Argument("start", location="json", required=True, help="Start is required"),
        Argument("description", location="json", required=False),
        Argument("stop", location="json", required=False)
    )
    @jwt_required()
    def post(name, start, description, stop):
        user_id = get_jwt_identity()['id']

        timer = TimerRepository.create(
            user_id=user_id,
            name=name,
            start=start,
            description=description,
            stop=stop
        )

        return timer

    @staticmethod
    @marshal_with(timer_list_fields)
    @jwt_required()
    def get():
        timers = TimerRepository.all()

        return { "items": timers }
