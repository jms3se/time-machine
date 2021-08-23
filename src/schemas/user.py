from flask_restful import fields

user_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "email": fields.String
}

user_login_fields = {
    "user": user_fields,
    "access_token": fields.String
}

user_list_fields = {
    "items": fields.List(fields.Nested(user_fields), attribute="items"),
}
