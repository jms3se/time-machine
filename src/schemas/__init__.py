from flask_marshmallow import Marshmallow

ma = Marshmallow()

from .user import user_fields
from .user import user_list_fields
from .user import user_login_fields

from .timer import timer_fields
from .timer import timer_list_fields

from .tag import tag_fields
from .tag import tag_list_fields

from .project import project_fields
from .project import project_list_fields
