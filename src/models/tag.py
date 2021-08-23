from . import db
from . import Base

timers = db.Table("timer_tag", db.Model.metadata,
    db.Column("timer_id", db.Integer, db.ForeignKey("timer.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True)
)

class Tag(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    available = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    timers = db.relationship("Timer", secondary=timers, backref=db.backref("tags", lazy=True))

    def __init__(self, user_id, name, description):
        self.user_id = user_id
        self.name = name
        self.description = description
