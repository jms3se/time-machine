from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from utils import generate_hash
from utils import check_hash

class UserResource(Resource):
    @staticmethod
    def get():
        user = UserRepository.get()
        return jsonify({"user": user})
