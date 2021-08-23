from flask_restful import fields

project_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String
}

project_list_fields = {
    "items": fields.List(fields.Nested(project_fields), attribute="items"),
}
