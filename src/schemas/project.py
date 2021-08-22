from . import ma

class ProjectSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description")

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)
