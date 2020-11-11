### server for HB capstone PT Remix app

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'SECRETKEY'
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View Homepage"""

    # view homepage with 

    return render_template("homepage.html")


@app.route("/")
def user_login():
    """User can log into existing account"""

    # needs
    # get user input of email and pw
    # check against valid account details
    # flash messages
    
    #redirects to routine builder page
    return redirect("/build-routine")


@app.route("/")
def create_account():
    """User can create a new account"""

    # needs
    # get user input of email and pw
    # check if existing account
    # add those to DB
    # flash messages

    # redirects to same page. should render homepage template instead?
    return redirect("/")

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

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')