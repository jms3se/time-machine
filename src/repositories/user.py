from models import User

class UserRepository:
    @staticmethod
    def create(name, email, password):
        user = User(name, email, password)

        user.save()

        return user

    @staticmethod
    def update(self, id, name):
        user = self.get(id=id).one()
        user.name = name

        user.save()

        return user

    @staticmethod
    def get(id):
        return User.query.filter_by(id=id)

    @staticmethod
    def getByEmail(email):
        user = User.query.filter_by(email=email).first()

        return user
