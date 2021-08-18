from datetime import datetime

from . import db, hybrid_method, hybrid_property
from utils import generate_hash, check_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    _password_hash = db.Column(db.String(128))

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

    def save(self):
        db.session.add(self)
        db.session.commit()
