### server for HB capstone PT Remix app

from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for)
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, User, Exercise, Routine, InjuryType
import os
import crud
import secrets
# StrictUndefined means that it will complain if I try to use something in jinja that I haven't defined
from jinja2 import StrictUndefined

app = Flask(__name__)
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

    return render_template("homepage.html")


@app.route("/", methods=["POST"])
def user_login_or_register():
    """User can log into existing account"""
    print("Login is go!")

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
            return redirect("/build-routine", session=session)
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
        return redirect(url_for("homepage"))
 

@app.route("/build-routine", methods=["GET"])
def view_builder_page():
    """View routine builder page"""
    print("builder is go")

    injuries = crud.get_all_injuries()

    # all that's needed here is to render the template
    return render_template("build_routine.html", injuries=injuries)


@app.route("/build-routine", methods=["POST"])
def build_new_routine():
    """Get info from form and generate a brand new PT routine"""
    print("new routine is go")
    
    # get user input from the form
    injury = request.form.get("injury-type")
    duration = request.form.get("duration")
    print("check form name/details")
    # have to update algo to include this
    # has_equip = request.form.get("equip")

    new_routine = crud.build_routine()

    routine_id = new_routine.routine_id

    # needs
    # get user inputs of time, injury type, equipment
    # on click, run relevant queries and

    # takes us to the routine page
    return redirect(f"/routine/{routine_id}")

@app.route("/routine/<routine_id>")
def view_routine(routine_id):
    """View details of one specific routine"""

    routine = Routine.query.get(routine_id)

    ex_for_routine = crud.get_exercises_by_routine(routine_id)

    # for exercise in ex_for_routine:
    #     reps = 

    return render_template("routine.html", exercises=ex_for_routine)


@app.route("/all-exercises")
def view_all_exercises():
    """View a list of all exercises"""

    # needs query for all exercises
    exercises = crud.get_all_exercises()

    return render_template("all_exercises.html", exercises=exercises)


@app.route("/your-routines")
def view_user_routines():
    """View a list of user's past routines"""

    # query to find all routines by user
    # have to make sure it only works based on user session

    return render_template("routine_list.html")


@app.route("/logout")
def user_logout():
    """Clears sessions and logs user out"""

    # click logout button, get routed back to home

    return redirect("/")


############FUNCTIONS#############################


#########################RUN IT##########################

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')