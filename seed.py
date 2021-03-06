"""Script to seed database."""

import os
# import json
# from random import choice, randint
# from datetime import datetime

import crud
from model import connect_to_db, db, User, Exercise, InjuryType, Routine
import server
from datetime import datetime

# always drop then create
os.system('dropdb ptremix')
os.system('createdb ptremix')

# connect to the database and set up models with db.create_all
connect_to_db(server.app)
db.create_all()

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
        duration=4,
        equip_req=False,
        exercise_type="endurance",
        freq=3,
        max_reps=20,
        img="/static/img/crab-walk.jpg")
    db.session.add(ex1)

    ex2 = Exercise(name="Ankle Flex with Resistance Band",
        description="With one end of the resistance band looped around the ball of the foot, and the other held in place by your hand, or tied to a stable object, pull against the band using your ankle. Hold for 3 seconds, then release.", 
        duration=5,
        equip_req=True,
        exercise_type="strength",
        freq=7,
        max_reps=20,
        img="/static/img/ankle-flex.jpg")
    db.session.add(ex2)

    ex3 = Exercise(name="Ankle Circles",
        description="Slowly rotate your ankle clockwise. Repate counterclockwise.",
        duration=3,
        equip_req=False,
        exercise_type="flexibility",
        freq=7,
        max_reps=20,
        img="/static/img/ankle-circles.jpg")
    db.session.add(ex3)

    ex4 = Exercise(name="Squats (supported)",
        description="Stand with feet shoulder-width apart, in front of a stable support for balance if needed. Slowly bend your knees and lower your body toward the floor. Your body weight should be mostly directed your the heels of your feet. Return to standing.",
        duration=5,
        equip_req=False,
        exercise_type="strength",
        freq=3,
        max_reps=10,
        img="/static/img/supported-squat.jpg")
    db.session.add(ex4)

    ex5 = Exercise(name="Step Up",
        description="Start by standing in front of a step/step stool with both feet on the ground. Step up the step with one leg and then with the other. Return to starting position by taking a step back toward the floor leading with the same leg you started with.",
        duration=3,
        equip_req=True,
        exercise_type="balance",
        freq=4,
        max_reps=20,
        img="/static/img/step-up.jpg")
    db.session.add(ex5)

    ex6 = Exercise(name="Standing Heel Raises",
        description="Stand in front of a counter or other surface at about waist height. Rise up on your toes and lift your heels off the ground. Start with lifting only a couple inches off the ground, then progress, as strength allows. Lower back to the floor slowly. Start by shifting weight onto uninjured foot, then shift to even weight distribution once you've reached the top of the lift. Try to stay even as you lower back down.",
        duration=1,
        equip_req=False,
        exercise_type="strength",
        freq=7,
        max_reps=20,
        img="/static/img/heel-raise.jpg")
    db.session.add(ex6)

    ex7 = Exercise(name="Walking",
        description="Concentrate on form, rather than endurance or speed. Focus on making sure strides are even in length, and roll all the way through your injured foot if possible (stead of limping). Take it slow, take shorter strides to start.",
        duration=2,
        equip_req=False,
        exercise_type="endurance",
        freq=7,
        max_reps=30,
        img="/static/img/walking.jpg")
    db.session.add(ex7)

    ex8 = Exercise(name="Arch Lifts",
        description="Start with both feet on the floor. While pressing your toes and heels into the floor, try to peel the arch of your foot off the floor. Hold for 2 seconds, release slowly.",
        duration=3,
        equip_req=False,
        exercise_type="flexibility",
        freq=7,
        max_reps=15,
        img="/static/img/arch-lift.jpg")
    db.session.add(ex8)
    
    ex9 = Exercise(name="Toe Yoga",
        description="Sit with knees over ankles. Keep ball and heel of the foot on the floor at all times. Lift the big toe, presisng the other toes into the floor. Hold for 5 seconds. Alternate by pressing the big toes into the floor, while lifting all other toes and hold for 5 seconds.",
        duration=6,
        equip_req=False,
        exercise_type="flexibility",
        freq=7,
        max_reps=20,
        img="/static/img/toe-yoga.jpg")
    db.session.add(ex9)

    ex10 = Exercise(name="Seated Calf Stretch",
        description="While sitting, use a towel or other strap (without stretch) looped around the base of your foot. Gently pull the towel taut, and press against it with your foot. You should feel a stretch along the back of your leg. Attempt to straighten your knee for added stretch, if it's comfortable. Hold for 1 minute.",
        duration=60,
        equip_req=True,
        exercise_type="flexibility",
        freq=7,
        max_reps=1,
        img="/static/img/seated-calf-stretch.jpg")
    db.session.add(ex10)

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

    inj4 = InjuryType(name="Shin splints",
        location="leg")
    db.session.add(inj4)

    inj5 = InjuryType(name="Lower back pain",
        location="lower back")
    db.session.add(inj5)
    
    inj6 = InjuryType(name="Tennis elbow",
        location="elbow")
    db.session.add(inj6)
    
    inj7 = InjuryType(name="Achilles tendinitis",
        location="leg")
    db.session.add(inj7)


    db.session.commit()

def create_routine():
    """Makes a new routine object"""

    r1 = Routine(user_id=1, duration=10, date_created=datetime.now())
    db.session.add(r1)

    r2 = Routine(user_id=1, duration=20, date_created=datetime.now())
    db.session.add(r2)

    r3 = Routine(user_id=1, duration=5, date_created=datetime.now())
    db.session.add(r3)

    db.session.commit()

def create_inj_ex_relationships():

    crud.add_injury_to_exercises(1, [1, 2, 3, 4])
    crud.add_injury_to_exercises(2, [5, 6, 7, 8])
    crud.add_injury_to_exercises(3, [2, 4, 6, 8])

def create_routine_ex_relationships():

    crud.add_exercise_to_routine(1, 1)
    crud.add_exercise_to_routine(2, 2)
    crud.add_exercise_to_routine(2, 3)

def add_some_test_ex_inj_relationships():

    crud.add_injury_to_exercises(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# call functions to create data
create_user()
create_exercise()
create_injury_type()
create_routine()
create_inj_ex_relationships()
create_routine_ex_relationships()
add_some_test_ex_inj_relationships()