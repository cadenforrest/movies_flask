from flask_login import UserMixin
from __init__ import db

movie_identifier = db.Table(
    "movie_identifier",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("movie_id", db.Integer, db.ForeignKey("movies.id")),
)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False, index=True)
    year = db.Column(db.Integer, index=True)
    cast = db.Column(db.String(100))
    genres = db.Column(db.String(100))

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "cast": self.cast,
            "genres": self.genres,
        }
