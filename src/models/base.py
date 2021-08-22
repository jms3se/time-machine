from . import db

class Base():
    def save(self):
        self.available = True
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        self.available = False
        db.session.commit()
