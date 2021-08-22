from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

db = SQLAlchemy()

from .base import Base
from .user import User
from .timer import Timer
from .tag import Tag
