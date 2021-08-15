from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

timer_identifier = db.Table("timer_identifier", db.Model.metadata,
    db.Column("tag_id", db.Integer, db.ForeingKey("tag.id")),
    db.Column("timer_id", db.Integer, db.ForeingKey("timer.id"))
)

from .user import User
