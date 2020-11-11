"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

# always drop then create
os.system('dropdb ptremix')
os.system('createdb ptremix')

# connect to the database and set up models with db.create_all
model.connect_to_db(server.app)
model.db.create_all()


# Then, load data from data/movies.json and save it to a variable:
# with open('data/movies.json') as f:
#     movie_data = json.loads(f.read())

# movies_in_db = []
# for movie in movie_data:
#     title, description, poster_path = (movie['title'],
#                                     movie['overview'],
#                                     movie['poster_path'])
#     release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

#     db_movie = crud.create_movie(title,
#                                  description,
#                                  release_date,
#                                  poster_path)
#     movies_in_db.append(db_movie)


# for n in range(10):
#     email = f'user{n}@test.com' 
#     password = 'test'

#     user = crud.create_user(email, password)

#     for _ in range(10):
#         random_movie = choice(movies_in_db)
#         score = randint(1, 5)

#         crud.create_rating(user, random_movie, score)