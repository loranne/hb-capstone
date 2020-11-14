### server for HB capstone PT Remix app

from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for)
from model import connect_to_db, User, Exercise, Routine, InjuryType
import os
import crud
import secrets
# StrictUndefined means that it will complain if I try to use something in jinja that I haven't defined
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "SECRETKEY"
# secrets.token_urlsafe(16)
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View Homepage"""
    print("Homepage is go!")
    print(request)

    flash("Hi Katie!")

    return render_template("homepage.html")


@app.route("/", methods=["POST"])
def user_login_or_register():
    """User can log into existing account"""
    print("Login is go!")

    if request.form.get("login"):
        email = request.form.get("email")
        password = request.form.get("password")

        user = crud.get_user_by_email(email)
        print(user)
        is_password_correct = crud.validate_user_password(user, password)
        print(is_password_correct)

        # session["user"] = user.user_id
        print(request.form)
        
        if is_password_correct:
            print("is_password_correct")
            flash("Welcome Back!")
            return redirect("/build-routine")
        else:
            print("or else!")
            flash("No for that email address. Please create an account.")
            return redirect(url_for("homepage"))
        
        # #redirects to routine builder page
        # return redirect("/build-routine")
    
    if request.form.get("register"):

        # get user input of email and pw
        # check if existing account
        # add those to DB (crud function)
        # flash messages

        email = request.form.get("email")
        password = request.form.get("password")

        user = crud.get_user_by_email(email)

        if user:
            flash("An account already exists for that email address. Please log in or try again.")
            print("User is yes")
        
        else: 
            crud.create_user(email, password)
            flash("Account created! Please enter your info to log in.")
            print("User is no")

        # redirects to same page. is this the right way to do this?
        return redirect(url_for("homepage"))
 

@app.route("/build-routine")
def view_builder_page():
    """View routine builder page"""

    # all that's needed here is to render the template
    return render_template("build_routine.html")


@app.route("/build-routine")
def build_new_routine():
    """Generate a brand new PT routine"""

    # needs
    # get user inputs of time, injury type, equipment
    # on click, run relevant queries and

    # takes us to the routine page
    return redirect("/routine/{routine_id}")


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

    # 