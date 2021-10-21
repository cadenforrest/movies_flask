import sys 
import os
from movies_table import db, Movie 
import json

def create_movies_db(): 
  """read JSON data from movies.json and populate the database with the data"""
  #open the movies.json file and populate the database with movie objects
  db.session.delete
  f = open('movies.json', encoding='utf-8')
  data = json.loads(f.read())
  print(data)
  n = 0
  for movie in data: 
    m = Movie(title = movie['title'], year = movie['year'], cast = json.dumps(movie['cast']), genres = json.dumps(movie['genres']))
    db.session.add(m)
    print ("added!")
    n = n+1
  db.session.commit()
  print(f'Added {n} movies to database.')


if __name__ == '__main__': 
  create_movies_db()

