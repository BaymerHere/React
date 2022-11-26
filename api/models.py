from . import db

class Movie(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(500))
    image = db.Column(db.String(500))
    rating = db.Column(db.Integer)
