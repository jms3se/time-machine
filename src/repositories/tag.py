from werkzeug.exceptions import NotFound

from models import Tag

class TagRepository:
    @staticmethod
    def create(user_id, name, description):
        tag = Tag(user_id, name, description)

        tag.save()

        return tag

    @staticmethod
    def get(id):
        tag = Tag.query.filter_by(id=id, available=True).first()

        if not tag:
            raise NotFound("tag not found")

        return tag

    @staticmethod
    def all():
        return Tag.query.filter_by(available=True)

    @staticmethod
    def update(id, name, description):
        tag = Tag.query.filter_by(id=id, available=True).first()

        if not tag:
            raise NotFound("tag not found")

        tag.name = name
        tag.description = description

        tag.update()

        return tag

    @staticmethod
    def delete(id):
        tag = Tag.query.filter_by(id=id, available=True).first()

        if not tag:
            raise NotFound("tag not found")

        tag.delete()

        return tag
