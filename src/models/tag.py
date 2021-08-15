from . import db, timer_identifier
from utils import generate_hash, check_hash

class Tag(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeingKey("user.id"))
    timers = db.relationship("Timer", secondary=timer_identifier)

    def __init__(self, name, description, start, stop):
        self.name = name
        self.description = description
        self.start = start
        self.stop = stop
