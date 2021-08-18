from . import db

from utils import generate_hash, check_hash

timers = db.Table("timers", db.Model.metadata,
    db.Column("timer_id", db.Integer, db.ForeignKey("timer.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True)
)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    timers = db.relationship("Timer", secondary=timers, backref=db.backref("tags", lazy=True))

    def __init__(self, name, description, start, stop):
        self.name = name
        self.description = description
        self.start = start
        self.stop = stop
