from flask_marshmallow import Marshmallow

ma = Marshmallow()

from .user import user_schema
from .user import users_schema

from .timer import timer_schema
from .timer import timers_schema
