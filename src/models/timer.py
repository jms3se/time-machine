from . import db

from utils import generate_hash, check_hash

class Timer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    start = db.Column(db.Date)
    stop = db.Column(db.Date)
    available = db.Column(db.Bool)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, name, description, start, stop):
        self.name = name
        self.description = description
        self.start = start
        self.stop = stop

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        self.available = False
        db.session.commit()
