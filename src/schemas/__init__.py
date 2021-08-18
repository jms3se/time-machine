from flask_marshmallow import Marshmallow

ma = Marshmallow()

from .user import user_schema
from .user import users_schema
