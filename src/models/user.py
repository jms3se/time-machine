from datetime import datetime

from . import db
from . import hybrid_property
from . import Base
from utils import generate_hash
from utils import check_hash

class User(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    _password_hash = db.Column(db.String(128))
    available = db.Column(db.Boolean)

    timers = db.relationship("Timer", backref="user", lazy=True)
    tags = db.relationship("Tag", backref="user", lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @hybrid_property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, password):
        self._password_hash = generate_hash(password)

    def verify_password(self, password):
        return check_hash(self._password_hash, password)
