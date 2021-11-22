from __init__ import db
from models import Movie
import json


def create_movies_db():
    """read JSON data from movies.json and populate the database with the data"""
    # open the movies.json file and populate the database with movie objects
    db.session.delete
    f = open("movies.json", encoding="utf-8")
    data = json.loads(f.read())
    n = 0
    for movie in data:
        # remove disallowed characters from cast and genres string
        disallowed_characters = '"[]'
        cast = json.dumps(movie["cast"])
        genres = json.dumps(movie["genres"])

        for character in disallowed_characters:
            cast = cast.replace(character, "")
            genres = genres.replace(character, "")

        m = Movie(title=movie["title"], year=movie["year"], cast=cast, genres=genres)
        db.session.add(m)
        print("added!")
        n = n + 1
    db.session.commit()
    print(f"Added {n} movies to database.")
