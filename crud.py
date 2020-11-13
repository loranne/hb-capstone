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

def create_routine()

def create_exerciseinjury_rship():
    """Sets up relationship between exercise and injury"""

    # NEED HALP




