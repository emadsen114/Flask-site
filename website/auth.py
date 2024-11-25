#website routes 

from flask import Blueprint

# we are defining that this is the bluerpint of our application

auth = Blueprint('auth', __name__)

@auth.route('/login') # decorator
def login():
    return "<h1>Login</h1>"

@auth.route('/logout') # decorator
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign-up') # decorator
def sign_up():
    return "<h1>Sign Up</h1>"