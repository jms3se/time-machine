from flask_restful import fields

tag_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String
}

tag_list_fields = {
    "items": fields.List(fields.Nested(tag_fields), attribute="items"),
}
