from werkzeug.exceptions import NotFound

from models import Timer

class TimerRepository:
    @staticmethod
    def create(user_id, name, start, description, stop):
        timer = Timer(user_id, name, start, description, stop)

        timer.save()

        return timer

    @staticmethod
    def get(id):
        timer = Timer.query.filter_by(id=id, available=True).first()

        if not timer:
            raise NotFound("timer not found")

        return timer

    @staticmethod
    def all():
        return Timer.query.filter_by(available=True)

    @staticmethod
    def update(id, name, start, description, stop):
        timer = Timer.query.filter_by(id=id, available=True).first()

        if not timer:
            raise NotFound("timer not found")

        timer.name = name
        timer.start = start
        timer.description = description
        timer.stop = stop

        timer.update()

        return timer

    @staticmethod
    def delete(id):
        timer = Timer.query.filter_by(id=id, available=True).first()

        if not timer:
            raise NotFound("timer not found")

        timer.delete()

        return timer
