from werkzeug.exceptions import NotFound

from models import Timer
from models import Project

class TimerProjectRepository:
    @staticmethod
    def create(id, project_id):
        timer = Timer.query.filter_by(id=id, available=True).first()
        project = Project.query.filter_by(id=project_id, available=True).first()

        timer.projects.append(project)

        timer.save()

        return {
            "project_id": project.id,
            "timer_id": timer.id
        }

    @staticmethod
    def get(id):
        timer = Timer.query.filter_by(id=id, available=True).first()

        if not timer:
            raise NotFound("timer not found")

        return timer.projects

    @staticmethod
    def delete(id, project_id):
        timer = Timer.query.filter_by(id=id, available=True).first()
        project = Project.query.filter_by(id=project_id, available=True).first()

        if not timer or not project:
            raise NotFound("not found")

        timer.projects.remove(project)

        timer.update()

        return timer
