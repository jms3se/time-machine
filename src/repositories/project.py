from werkzeug.exceptions import NotFound

from models import Project

class ProjectRepository:
    @staticmethod
    def create(user_id, name, description):
        project = Project(user_id, name, description)

        project.save()

        return project

    @staticmethod
    def get(id):
        project = Project.query.filter_by(id=id, available=True).first()

        if not project:
            raise NotFound("project not found")

        return project

    @staticmethod
    def all():
        return Project.query.filter_by(available=True)

    @staticmethod
    def update(id, name, description):
        project = Project.query.filter_by(id=id, available=True).first()

        if not project:
            raise NotFound("project not found")

        project.name = name
        project.description = description

        project.update()

        return project

    @staticmethod
    def delete(id):
        project = Project.query.filter_by(id=id, available=True).first()

        if not project:
            raise NotFound("project not found")

        project.delete()

        return project
