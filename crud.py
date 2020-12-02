# CRUD operations and queries for page content goes here

from model import db, Exercise, User, InjuryType, ExerciseInjury, ExerciseRoutine, Routine
from datetime import datetime 
import random
import utilities

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

    #DONE: Find out if user_id is all I need to pass in here. The only other things that go here are routine_id and date created
    # I'm not sure about datetime here

    routine = Routine(user_id=user_id, duration=duration, date_created=datetime)

    db.session.add(routine)
    db.session.commit()
    
    return routine

def build_routine(user_id, duration, inj_type_id, datetime=datetime.now()):
    """Creates new routine with specific parameters"""

    # calls function to get previous routine object. yes, we have the object
    prev_routine = get_prev_routine(user_id)
    utilities.print_color(prev_routine)

    # List of all possible exercises by injury
    exercise_pool = get_exercises_by_injury(inj_type_id)
    #call list on exercise_pool to treat like a python list of objects
    exercise_pool = list(exercise_pool)

    for exercise in exercise_pool:
        if exercise in prev_routine.exercises:
            relationship = ExerciseRoutine.query.filter_by(exercise_id=exercise.exercise_id, routine_id=prev_routine.routine_id).first()
            if relationship.exercise_pain == "negative":
                exercise_pool.remove(exercise)

    duration = int(duration)
    # 2 exercises per 5 min block 
    num_exercises = int(duration / 5 * 2)
    utilities.print_color(f"No. of exercises is {num_exercises}")

    time_per_exercise = int((duration / num_exercises) * 60)
    print(time_per_exercise)

    # the routine I'm adding exercises to
    routine = create_routine(user_id, duration, datetime)
    print(routine)

    # exercises to choose from = all exercises based on injury type
    exercises = exercise_pool
    print(exercises)
    
    num_exercises = min(num_exercises, len(exercise_pool))
    print(num_exercises)
    

    # variable exercise_choice should be list of randomly chosen exercises from 
    # line above, based on num_exercises
    exercise_choice = random.sample(exercises, k=num_exercises)
    print(exercise_choice)

    #DONE: decide if it makes more sense to call add_exercises_to_routine within
    #loop, or before loop—within wins
    
    # set up exerciseroutine relationship for each exercise chosen

    # loop over that list of randomly chosen exercises
    #DONE: FIX MATH
    for exercise in exercise_choice:
        add_exercise_to_routine(exercise.exercise_id, routine.routine_id)
        reps = int(time_per_exercise / exercise.duration)
        # need to hang onto max_reps as a variable that *might* change, if certain
        # conditions are met
        max_reps = exercise.max_reps
        if exercise in prev_routine.exercises:
            # sets relationship variable
            relationship = ExerciseRoutine.query.filter_by(exercise_id=exercise.exercise_id, routine_id=prev_routine.routine_id).first()
            if relationship.exercise_pain == "neutral":
                max_reps = int(max_reps / 2)
        # if that exceeds max reps, reduce to max reps
        if reps > max_reps:
            reps = max_reps

        relationship = ExerciseRoutine.query.filter_by(exercise_id=exercise.exercise_id, routine_id=routine.routine_id).first()

        #TODO: if relationship, just in case there is no match for ex and routine ids
        if relationship:
            relationship.exercise_reps = reps
            print(relationship.exercise_reps)
            db.session.commit()
        else: 
            print("No such routine-exercise relationship.")
        # append reps to exerciseroutine table, based on exercise_id and routine_id

    # return this so I can then grab the routine_id easily for making new page
    return routine


def set_pain_level_for_exercise(pain_level, exercise_id, routine_id):
    """sets exercise_pain in ExerciseRoutine based on user input"""
    
    # selects the appropriate record to add pain level to
    exroutine = ExerciseRoutine.query.filter_by(exercise_id=exercise_id, routine_id=routine_id).one()
    # makes the pain level addition/replacement if it's already there
    exroutine.exercise_pain = pain_level
    db.session.commit()

    return exroutine

####################QUERIES/GETTING INFO#######################

def logout_user():
    """Logs user out of app and removes user from flask session"""

    # user_id = session["user"]

    # user = User.query.get(user_id)

    del session["user"]

def get_prev_routine(user_id):
    """Get the last routine that this user generated"""

    prev_routine = Routine.query.order_by(Routine.date_created.desc()).filter(Routine.user_id==user_id).first()

    return prev_routine


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


def set_exercise_pain(exercise_id, routine_id, pain_level):
    """Sets the pain level for exerciseroutine relationship"""

    ex_routine = ExerciseRoutine.query.filter(exercise_id=exercise_id, routine_id=routine_id).first()

    ex_routine.exercise_pain = pain_level


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