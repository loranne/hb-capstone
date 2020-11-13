### server for HB capstone PT Remix app

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import os
import crud
import secrets
# StrictUndefined means that it will complain if I try to use something in jinja that I haven't defined
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View Homepage"""

    return render_template("homepage.html")


@app.route("/")
def user_login():
    """User can log into existing account"""

    # TODO:
    # get user input of email and pw
    # check against valid account details
    # flash messages
    
    #redirects to routine builder page
    return redirect("/build-routine")


@app.route("/", methods=["POST"])
def create_account():
    """User can create a new account"""
    
    # get user input of email and pw
    # check if existing account
    # add those to DB (crud function)
    # flash messages

    email = request.form.get("email")
    password = request.form.get("password")

    user = get_user_by_email(email)

    if user:
        flash("An account already exists for that email address. Please log in or try again.")
    
    else: 
        crud.create_user(email, password)
        flash("Account created! Please enter your info to log in.")

    # redirects to same page. is this the right way to do this?
    return redirect("/")

@app.route('/users')
def login_user():

    email = request.form.get('login-email')
    password = request.form.get('login-password')

    user_email = crud.get_user_by_email(email)
    user_password = crud.validate_user_password(password)

    session['user'] = User.user_id
    
    if user:
        flash('Welcome Back!')
    else:
        flash('No account by that name! Please create an account.')

    return redirect('/') 

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

    return render_template("all_exercises.html")


@app.route("/your-routines")
def view_user_routines():
    """View a list of user's past routines"""

    # query to find all routines by user
    # have to make sure it only works based on user session

    return render_template("routine_list.html")

@app.route("/logout")
def user_logout():
    """User logs out of account"""

    # click logout button, get routed back to home

    return redirect("/")

############FUNCTIONS#############################

def get_user_by_email(email):
    """Return a user by email"""

    # returns one user with the given email address. should work because email
    # address has to be unique
    return User.query.filter(User.email == email).one()


def validate_user_password(password):
    """Checks for valid password"""

    # returns first instance of user password equalling the password entered
    return User.query.filter(User.password == password).first()


#########################RUN IT##########################

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')

    # 