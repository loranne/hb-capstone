# CRUD operations and queries for page content goes here

from model import db, Exercise, User, InjuryType, ExerciseInjury, ExerciseRoutine, Routine
from datetime import datetime 
import random

import server
from sqlalchemy.orm.exc import NoResultFound
# from flask import session

#################CREATING RECORDS######################
def create_user(email, password):
    """Create and return a new user record"""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_exercise(name, description, duration, equip_req, freq, img="/404_smile.jpg"):
    """Create and return a new exercise record"""

    exercise = Exercise(name=name, description=description, duration=duration, 
        equip_req=equip_req, freq=freq, img=img)
    
    db.session.add(exercise)
    db.session.commit()

    return exercise


def create_injury_type(name, location):
    """Create and return a new injury type record."""

    injury_type = InjuryType(name=name, location=location)

    db.session.add(injury_type)
    db.session.commit()

    return injury_type


def create_routine(user_id, duration, datetime=datetime.now()):
    """Create a new routine record"""

    #TODO: Find out if user_id is all I need to pass in here. The only other things that go here are routine_id and date created
    # I'm not sure about datetime here

    routine = Routine(user_id=user_id, duration=duration, date_created=datetime)

    db.session.add(routine)
    db.session.commit()
    
    return routine

def build_routine(user_id=1, duration=10, datetime=datetime.now(), inj_type_id=1):
    """Creates new routine with specific parameters"""

    # 2 exercises per block 
    num_exercises = int(duration / 5 / 2)
    print(f"No. of exercises is {num_exercises}")
    time_per_exercise = int((duration / num_exercises) * 60)
    print(time_per_exercise)

    

    # the routine I'm adding exercises to
    routine = create_routine(user_id, duration, datetime)
    print(routine)

    # exercises to choose from = all exercises based on injury type
    exercises = get_exercises_by_injury(inj_type_id)
    print(exercises)

    # variable exercise_choice should be list of randomly chosen exercises from 
    # line above, based on num_exercises
    exercise_choice = random.sample(exercises, k=num_exercises)
    print(exercise_choice)

    #TODO: decide if it makes more sense to call add_exercises_to_routine within
    #TODO: loop, or before loop
    
    # set up exerciseroutine relationship for each exercise chosen

    # loop over that list of randomly chosen exercises
    for exercise in exercise_choice:
        add_exercise_to_routine(exercise.exercise_id, routine.routine_id)
        reps = int(time_per_exercise / exercise.duration)
        print(reps)
        relationship = ExerciseRoutine.query.filter_by(exercise_id=exercise.exercise_id, routine_id=routine.routine_id).first()
        print(relationship)

        #TODO: if relationship, just in case there is no match for ex and routine ids
        relationship.exercise_reps = reps
        print(relationship.exercise_reps)
        db.session.commit()
        # append reps to exerciseroutine table, based on exercise_id and routine_id

    # return this so I can then grab the routine_id easily for making new page
    return routine


####################QUERIES/GETTING INFO#######################

def get_user_by_email(email):
    """Return a user by email"""

    # returns one user with the given email address. should work because email
    # address has to be unique
    try: 
        return User.query.filter(User.email == email).one()

    except NoResultFound:
        return None


def validate_user_password(user, password):
    """Checks for valid password"""

    # returns first instance of user password equalling the password entered
    return user.password == password

def get_all_exercises():
    """Gets all exercises in DB"""

    exercises = db.session.query(Exercise).all()

    return exercises


def get_all_injuries():
    """Gets all injury types in DB"""

    injuries = db.session.query(InjuryType).all()
    # could also do InjuryType.query.all()

    return injuries


def add_injury_to_exercises(injury_type_id, exercise_ids):
    """Adds injury-exercise relationship to association table"""
    
    #DONE: change to accept list input of exericse IDs. Make function for that

    # isolates injury based on id
    injury = InjuryType.query.get(injury_type_id)

    # looping over list of exercise ids passed in as arg
    for ex_id in exercise_ids:
        # gets the exercise object based on the id
        exercise = Exercise.query.get(ex_id)
        # appends the injury to that exercise
        exercise.injuries.append(injury)

    # commit all the appends to the db
    db.session.commit()
    
    # returns nothing

def add_exercise_to_routine(exercise_id, routine_id):
    """Adds list of exercises to routine. Works a lot like add injury to exercise"""

    routine = Routine.query.get(routine_id)
    exercise = Exercise.query.get(exercise_id)

    routine.exercises.append(exercise)

    # not doing a loop anymore, because loop will happen in routine builder
    # for ex_id in exercise_ids:
    #     exercise = Exercise.query.get(exercise_id)
    #     routine.exercises.append(exercise)
    
    db.session.commit()

def get_exercises_by_routine(routine_id):
    """Returns exercises from one routine"""

    ex_by_routine = Routine.query.get(routine_id).exercises

    return ex_by_routine


def get_exercises_by_injury(injury_id):
    """Returns all exercises applicable to a specific injury"""

    # now that I have the function on line 120 working, this one works, too
    ex_by_inj = InjuryType.query.get(injury_id).exercises

    # get list of objects
    return ex_by_inj

#TODO: Figure out what's going on with this function.
# def get_routines_by_user(user_id=session["user"]):
    """Get all routines for a given user"""

    # return Routine.query.get(user_id).all()