from werkzeug.exceptions import NotFound

from models import Tag
from models import Timer

class TimerTagRepository:
    @staticmethod
    def create(id, tag_id):
        timer = Timer.query.filter_by(id=id, available=True).first()
        tag = Tag.query.filter_by(id=tag_id, available=True).first()

        timer.tags.append(tag)

        timer.save()

        return {
            "tag_id": tag.id,
            "timer_id": timer.id
        }

    @staticmethod
    def get(id):
        timer = Timer.query.filter_by(id=id, available=True).first()

        if not timer:
            raise NotFound("timer not found")

        return timer.tags

    @staticmethod
    def delete(id, tag_id):
        timer = Timer.query.filter_by(id=id, available=True).first()
        tag = Tag.query.filter_by(id=tag_id, available=True).first()

        if not timer or not tag:
            raise NotFound("not found")

        timer.tags.remove(tag)

        timer.update()

        return timer
