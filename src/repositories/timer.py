from models import Timer

class TimerRepository:
    @staticmethod
    def create(user_id, name, start, description, stop):
        timer = Timer(user_id, name, start, description, stop)

        timer.save()

        return timer

    @staticmethod
    def get(id):
        return Timer.query.filter_by(id=id).first()

    @staticmethod
    def all():
        return Timer.query.all()

    @staticmethod
    def update(id, name, start, description, stop):
        timer = Timer.query.get(id=id)

        timer.name = name
        timer.start = start
        timer.description = description
        timer.stop = stop

        timer.update()

        return timer

    @staticmethod
    def delete(id):
        timer = Timer.query.get(id=id)

        timer.delete()

        return timer
