from flask_marshmallow import Marshmallow

ma = Marshmallow()

from .user import user_schema
from .user import users_schema

from .timer import timer_schema
from .timer import timers_schema

from .tag import tag_schema
from .tag import tags_schema

from .project import project_schema
from .project import projects_schema
