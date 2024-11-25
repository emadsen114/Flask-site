#website routes 

from flask import Blueprint, render_template
# we are defining that this is the bluerpint of our application

views = Blueprint('views', __name__)

@views.route('/') # decorator 
def home(): # the function , these go together 
    return render_template("home.html")


