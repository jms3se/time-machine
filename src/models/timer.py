from . import db
from . import Base

class Timer(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    start = db.Column(db.Date)
    description = db.Column(db.String(200))
    stop = db.Column(db.Date)
    available = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, user_id, name, start, description = "", stop = ""):
        self.user_id = user_id
        self.name = name
        self.start = start
        self.description = description
        self.stop = stop
