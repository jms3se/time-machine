from . import db
from . import Base

timers = db.Table("timer_project", db.Model.metadata,
    db.Column("timer_id", db.Integer, db.ForeignKey("timer.id"), primary_key=True),
    db.Column("project_id", db.Integer, db.ForeignKey("project.id"), primary_key=True)
)

class Project(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    available = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    timers = db.relationship("Timer", secondary=timers, backref=db.backref("projects", lazy=True))

    def __init__(self, user_id, name, description = ""):
        self.user_id = user_id
        self.name = name
        self.description = description
