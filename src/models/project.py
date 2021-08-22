from . import db
from . import Base

class Project(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    available = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, user_id, name, description = ""):
        self.user_id = user_id
        self.name = name
        self.description = description
