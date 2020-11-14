# CRUD operations and queries for page content goes here

from model import db, Exercise, User, InjuryType, ExerciseInjury, ExerciseRoutine
from datetime import datetime 

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


def create_ex_inj_relationship(inj_type_id, exercise_id):
    """Sets up relationship between exercise and injury."""

    #TODO: Figure out what I need to know about each exercise and injury in order to set this up.
    # NEED HALP

    exercise_injury = ExerciseInjury(inj_type_id=inj_type_id, exercise_id=exercise_id)

    db.session.add(exercise_injury)
    db.session.commit()

    return exercise_injury


def create_ex_routine_relationship(routine_id, exercise_id):
    """Sets up relationship between exercise and routine."""

    exercise_routine = ExerciseRoutine(routine_id=routine_id, exercise_id=exercise_id)

    db.session.add(exercise_routine)
    db.session.commit()

    return exercise_routine


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

#TODO: Figure out what's going on with this function.
# def get_routines_by_user(user_id=session["user"]):
    """Get all routines for a given user"""

    # return Routine.query.get(user_id).all()