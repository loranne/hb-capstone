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

def create_user():
    """Create some test users"""

    user1 = User(email="loranne.n@gmail.com", 
        password="1234007")
    db.session.add(user1)

    user2 = User(email="l.orannen@gmail.com", 
        password="1234007")
    db.session.add(user2)

    db.session.commit()

def create_exercise():
    """Create some test exercises"""

    ex1 = Exercise(name="Crab Walk", 
        description="With knees bent, step one foot out to the side, then bring the other foot to it. Continuing walking sideways like this for 20 steps, then switch sides.", 
        duration=2,
        equip_req=False,
        frequency=3)
    db.session.add(ex1)

    ex2 = Exercise(name="Ankle Flex with Resistance Band",
        description="With one end of the resistance band looped around the ball of the foot, and the other held in place by your hand, or tied to a stable object, pull against the band using your ankle. Hold for 3 seconds, then release.", 
        duration=5,
        equip_req=True,
        frequency=7)
    db.session.add(ex2)

    ex3 = Exercise(name="Ankle Circles",
        description="Slowly rotate your ankle clockwise. Repate counterclockwise.",
        duration=1,
        equip_req=False,
        frequency=7)
    db.session.add(ex3)

    db.session.commit()

def create_injury_type():
    """Create some test injury types"""

    inj1 = InjuryType(name="Trimalleolar fracture",
        location="ankle")
    db.session.add(inj1)

    inj2 = InjuryType(name="Torn meniscus",
        location="knee")
    db.session.add(inj2)

    inj3 = InjuryType(name="Carpal tunnel",
        location="wrist")
    db.session.add(inj3)

    db.session.commit()


# call functions to create data
create_user()
create_exercise()
create_injury_type()


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