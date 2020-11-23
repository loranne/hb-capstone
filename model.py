# Models for Hackbright capstone project: PT Remix
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random
import crud

db = SQLAlchemy()

class Exercise(db.Model):
    """An exercise"""

    __tablename__ = "exercises"

    exercise_id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String,
                        unique=True,
                        nullable=False)
    description = db.Column(db.Text,
                        nullable=False)
    duration = db.Column(db.Integer,
                        nullable=False)
    equip_req = db.Column(db.Boolean,
                        nullable=False)
    freq = db.Column(db.Integer)
    max_reps = db.Column(db.Integer,
                    nullable=False)
    img = db.Column(db.String)

    injuries = db.relationship("InjuryType", secondary="exercise_injury")
    # old way: exercise_injury = db.relationship("ExerciseInjury")
    routines = db.relationship("Routine", secondary="exercise_routine")
    # old way: exercise_routine = db.relationship("ExerciseRoutine")

    def __repr__(self):
        return f"<Exercise id={self.exercise_id} name={self.name}>"


class ExerciseInjury(db.Model):
    """An association between Exercise and Injury Type"""

    __tablename__ = "exercise_injury"

    exinj_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    inj_type_id = db.Column(db.Integer,
                        db.ForeignKey("injury_types.inj_type_id"))
    exercise_id = db.Column(db.Integer,
                        db.ForeignKey("exercises.exercise_id"))
    
    injury_types = db.relationship("InjuryType")
    exercises = db.relationship("Exercise")

    def __repr__(self):
        return f"<ExerciseInjury id={self.exinj_id} inj_type_id={self.inj_type_id} exercise_id={self.exercise_id}>"


class InjuryType(db.Model):
    """An injury type"""

    __tablename__ = "injury_types"

    inj_type_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String,
                        nullable=False)
    location = db.Column(db.String,
                        nullable=False)
    # description = db.Column(db.String)

    exercises = db.relationship("Exercise", secondary="exercise_injury")
    # old way: exercise_injury = db.relationship("ExerciseInjury")


    def __repr__(self):
        return f"<InjuryType id={self.inj_type_id} name={self.name} location={self.location}>"


class Routine(db.Model):
    """A routine containing exercises"""

    __tablename__ = "routines"

    routine_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.user_id"))
    duration = db.Column(db.Integer)
    date_created = db.Column(db.DateTime,
                        nullable=False)
    
    
    users = db.relationship("User")
    exercises = db.relationship("Exercise", secondary="exercise_routine")
    # old way: exercise_routine = db.relationship("ExerciseRoutine")

    def __repr__(self):
        return f"<Routine id={self.routine_id} date={self.date_created} user_id={self.user_id}>"
    

class ExerciseRoutine(db.Model):
    """An association between Exercise and Routine"""

    __tablename__ = "exercise_routine"

    exroutine_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    routine_id = db.Column(db.Integer,
                        db.ForeignKey("routines.routine_id"))
    exercise_id = db.Column(db.Integer,
                        db.ForeignKey("exercises.exercise_id"))
    # stores # reps per exercise. take this out if it fails...
    exercise_reps = db.Column(db.Integer,
                        nullable=False)
    
    # TODO: Figure out what needs to happen to the 2 lines below
    routines = db.relationship("Routine")
    exercises = db.relationship("Exercise")

    def __repr__(self):
        return f"<ExerciseRoutine id={self.exroutine_id} routine_id={self.routine_id} exercise_id={self.exercise_id}>"


class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String,
                        unique=True,
                        nullable=False)
    password = db.Column(db.String,
                        nullable=False)
    
    routines = db.relationship("Routine")

    def __repr__(self):
        return f"<User id={self.user_id} email={self.email}>"


def connect_to_db(flask_app, db_uri="postgresql:///ptremix", echo=True):
    """Connect to the DB"""
    
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

# for running model interactively and testing db
if __name__ == '__main__':
    from server import app
    # pulls in seed data
    import seed

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, echo=False)