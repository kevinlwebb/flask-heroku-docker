from app import db

class Book(db.Model):
    title = db.Column(db.String(64), primary_key=True, unique=True)
    author = db.Column(db.String(64))

    def __repr__(self):
        return '<Book {}>'.format(self.title)
