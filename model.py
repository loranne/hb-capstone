# Models for Hackbright capstone project: PT Remix
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "SECRETKEY"
# app.jinja_env.undefined = StrictUndefined

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
    frequency = db.Column(db.Integer)
    # reps = db.Column(db.Integer)
    img = db.Column(db.String)

    # exercise_injury = db.relationship("ExerciseInjury")
    injuries = db.relationship("InjuryType", secondary="exercise_injury")
    exercise_routine = db.relationship("ExerciseRoutine")

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
    # exercise_injury = db.relationship("ExerciseInjury")


    def __repr__(self):
        return f"<InjuryType id={self.inj_type_id} name={self.name} location={self.location}>"


class Routine(db.Model):
    """A routine containing exercises"""

    __tablename__ = "routines"

    routine_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    date_created = db.Column(db.DateTime,
                        nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.user_id"))
    
    users = db.relationship("User")
    exercise_routine = db.relationship("ExerciseRoutine")

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
    user_email = db.Column(db.String,
                        nullable=False)
    user_password = db.Column(db.String,
                        nullable=False)
    
    routines = db.relationship("Routine")

    def __repr__(self):
        return f"<User id={self.user_id} email={self.user_email}>"


def connect_to_db(flask_app, db_uri="postgresql:///ptremix", echo=True):
    """Connect to the DB"""
    
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')