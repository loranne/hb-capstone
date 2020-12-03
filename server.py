### server for HB capstone PT Remix app

from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for, jsonify)
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Exercise, Routine, InjuryType, ExerciseRoutine
import os
import crud
import secrets
from datetime import datetime
# StrictUndefined means that it will complain if I try to use something in jinja that I haven't defined
from jinja2 import StrictUndefined

# has my colorizer function
import utilities

app = Flask(__name__)
# need to adjust this one
app.secret_key = "SECRETKEY"
app.debug = True
toolbar = DebugToolbarExtension(app)
# secrets.token_urlsafe(16)
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View Homepage"""
    print("Homepage is go!")
    print(request)
    # utilities.print_color(session["user"])

    return render_template("homepage.html")


@app.route("/", methods=["POST"])
def user_login_or_register():
    """User can log into existing account"""
    utilities.print_color("Login is go!")
    # utilities.print_color(session["user"])

    # did user click the log in button? if yes:
    if request.form.get("login"):
        email = request.form.get("email")
        password = request.form.get("password")

        user = crud.get_user_by_email(email)
        print(user)
        is_password_correct = crud.validate_user_password(user, password)
        print(is_password_correct)

        # session["user"] = user.user_id
        print(request.form)
        
        # did user enter right pw? if yes:
        if is_password_correct:
            print("is_password_correct")
            flash("Welcome Back!")
            session["user"] = user.user_id
            # I have session returned here, after successful login. I think 
            # that'll let me keep it and use it and add to it!
            return redirect("/build-routine", session["user"])
        # if no:
        else:
            print("or else!")
            flash("No for that email address. Please create an account.")
            return redirect(url_for("homepage"))
    
    # did user click the register button? if yes:
    if request.form.get("register"):

        email = request.form.get("email")
        password = request.form.get("password")

        user = crud.get_user_by_email(email)

        # does a user with that email already exist? if yes:
        if user:
            flash("An account already exists for that email address. Please log in or try again.")
        # if no:
        else: 
            crud.create_user(email, password)
            flash("Account created! Please enter your info to log in.")

        # redirects to same page. is this the right way to do this?
        return redirect(url_for("homepage"), user=user)


@app.route("/goodbye")
def user_logout():
    utilities.print_color(session)
    utilities.print_color("test")
    """Calls user logout function from crud and displays goodbye message"""

    session.pop("user", None)

    return render_template("goodbye.html")
 

@app.route("/build-routine", methods=["GET"])
def view_builder_page():
    """View routine builder page"""
    flash(f"User id is: {session['user']}")
    utilities.print_color("builder is go")

    injuries = crud.get_all_injuries()

    # all that's needed here is to render the template
    return render_template("build_routine.html", injuries=injuries)


@app.route("/build-routine", methods=["POST"])
def build_new_routine():
    """Get info from form and generate a brand new PT routine"""
    utilities.print_color("new routine is go")
    
    # get user input from the form
    injury_name = request.form.get("injury")
    utilities.print_color(injury_name)
    injury = InjuryType.query.filter_by(name=injury_name).one()
    utilities.print_color(injury)
    # injury_id = injury.inj_type_id
    duration = request.form.get("duration")
    print("check form name/details")
    # have to update algo to include this
    # has_equip = request.form.get("equip")

    new_routine = crud.build_routine(session["user"], duration, injury.inj_type_id)

    routine_id = new_routine.routine_id

    # takes us to the routine page
    return redirect(f"/routine/{routine_id}")

@app.route("/routine/<routine_id>")
def view_routine(routine_id):
    """View details of one specific routine"""

    routine = Routine.query.get(routine_id)

    list_ex_for_routine = crud.get_exercises_by_routine(routine_id)

    # append ex_reps to exercise object in python
    # we're going to declare that there's a part of the exercise object in PYTHON, not the db
    # that is reps, add reps from ExerciseRoutine table into that slot
    # pluralize association table names

    for exercise in list_ex_for_routine:
        relationship = ExerciseRoutine.query.filter_by(exercise_id=exercise.exercise_id, routine_id=routine_id).first()
        exercise.reps = relationship.exercise_reps

    return render_template("routine.html", exercises=list_ex_for_routine, routine_id=routine_id)


@app.route("/routine/<routine_id>", methods=["POST"])
def update_exercise_pain(routine_id):
    """User clicks button, button changes and updates exercise_pain in ExerciseRoutine"""

    utilities.print_color(request.form.get("pain_level"))
    
    # gets pain level string from post request
    pain_level = request.form.get("pain_level")

    # gets the ID of the button from the post request
    id_string = request.form.get("id")
    
    # splits the ID string into a list
    list_of_id_parts = id_string.split("-")
    
    # gets the exercise id and routine ids out of that list
    ex_id = list_of_id_parts[1]
    rt_id = list_of_id_parts[2]

    # gets the right relationship record from the DB
    relationship = ExerciseRoutine.query.filter_by(exercise_id=ex_id, routine_id=rt_id).first()
    # adds the pain level info from the post request to the db and commits
    relationship.exercise_pain = pain_level
    utilities.print_color(pain_level)
    db.session.commit()

    utilities.print_color(relationship)
    return jsonify({"status": "okay"})


@app.route("/all-exercises")
def view_all_exercises():
    """View a list of all exercises"""

    # needs query for all exercises
    exercises = crud.get_all_exercises()

    return render_template("all_exercises.html", exercises=exercises)


@app.route("/your-routines")
def view_user_routines():
    """View a list of user's past routines"""

    user_id = session["user"]
    # simple query to get all routines for that user
    user_routines_by_time = Routine.query.order_by(Routine.date_created.desc()).filter_by(user_id=user_id)

    return render_template("routine_list.html", routines=user_routines_by_time)


############FUNCTIONS#############################


#########################RUN IT##########################

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')