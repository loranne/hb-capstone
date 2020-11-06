# server for HB capstone PT Remix app

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
# import crud
# from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'SECRETKEY'
# app.jinja_env.undefined = StrictUndefined

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')