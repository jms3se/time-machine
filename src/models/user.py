from . import db
from utils import generate_hash, check_hash
class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

    timers = db.relationship("Timer")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @password.setter
    def password(self, password):
        self.password = generate_hash(password)

    def verify_password(self, password):
        return check_hash(self.password, password)
