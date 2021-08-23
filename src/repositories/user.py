from sqlalchemy.exc import DatabaseError
from werkzeug.exceptions import BadRequest

from models import User

class UserRepository:
    @staticmethod
    def create(name, email, password):
        user = User(name, email, password)

        try:
            user.save()
        except DatabaseError:
            raise BadRequest("Invalid parameters")

        return user

    @staticmethod
    def get(id):
        return User.query.filter_by(id=id).first()

    @staticmethod
    def getByEmail(email):
        user = User.query.filter_by(email=email).first()

        return user
