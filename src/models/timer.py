from . import db

from utils import generate_hash, check_hash

class Timer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    start = db.Column(db.Date)
    stop = db.Column(db.Date)
    available = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, user_id, name, start, description = "", stop = ""):
        self.user_id = user_id
        self.name = name
        self.start = start
        self.description = description
        self.stop = stop

    def save(self):
        self.available = True
        db.session.add(self)
        db.session.commit()

    def update():
        db.session.commit()

    def delete(self):
        self.available = False
        db.session.commit()
