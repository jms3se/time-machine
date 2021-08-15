from . import db, timer_identifier
from utils import generate_hash, check_hash

class Timer(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ "timers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    start = db.Column(db.Datetime)

    user_id = db.Column(db.Integer, db.ForeingKey("user.id"))
    tags = db.relationship("Tag", secondary=timer_identifier)

    def __init__(self, name, description, start, stop):
        self.name = name
        self.description = description
        self.start = start
        self.stop = stop
