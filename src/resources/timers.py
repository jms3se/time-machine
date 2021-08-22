from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from schemas import timer_schema
from schemas import timers_schema
from repositories import TimerRepository
from utils import generate_hash
from utils import check_hash
from utils import parse_params

class TimersResource(Resource):
    @staticmethod
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

        return timer_schema.jsonify(timer)

    @staticmethod
    @jwt_required()
    def get():
        timers = TimerRepository.all()

        result = timers_schema.dump(timers)

        return jsonify(result)
