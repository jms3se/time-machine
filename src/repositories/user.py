from models import User

class UserRepository:
    @staticmethod
    def create(name, email, password):
        user = User(name, email, password)

        user.save()

        return user

    @staticmethod
    def get(id):
        return User.query.filter_by(id=id).first()

    @staticmethod
    def getByEmail(email):
        user = User.query.filter_by(email=email).first()

        return user
