# CRUD operations and queries for page content goes here

import model


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

    routine = Routine(user_id=user_id, duration=duration)


def create_ex_inj_relationship():
    """Sets up relationship between exercise and injury."""

    #TODO: Figure out what I need to know about each exercise and injury in order to set this up.
    # NEED HALP

    exercise_injury =

def create_ex_routine_relationship():
    """Sets up relationship between exercise and routine."""

    exercise_routine = ExerciseRoutine(routine_id=routine_id, exercise_id=exercise_id)

    db.session.add(exercise_routine)
    db.session.commit()

    return exercise_routine


