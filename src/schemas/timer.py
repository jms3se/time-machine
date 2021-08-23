from flask_restful import fields

timer_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "start": fields.String,
    "description": fields.String,
    "stop": fields.String,
}

timer_list_fields = {
    "items": fields.List(fields.Nested(timer_fields), attribute="items"),
}
