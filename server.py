# server for HB capstone PT Remix app

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'SECRETKEY'
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    '''View Homepage'''

    return render_template('homepage.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')

#####################"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
# import secrets

app = Flask(__name__)
app.secret_key = 'SECRETKEY'
app.jinja_env.undefined = StrictUndefined




# Replace this with routes and view functions!

@app.route('/')
def homepage():
    '''View Homepage'''

    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    """View all movies."""

    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """ Show details on a particular movie. """

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users')
def show_users():
    """View all users"""

    users = crud.get_users()

    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """View user profile"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)

@app.route('/users', methods=['POST'])
def register_user():

    email = request.form.get('create-email')
    password = request.form.get('create-password')

    user = crud.get_user_by_email(email)
    
    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')

@app.route('/')
def login_user():
    """User login"""

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

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')