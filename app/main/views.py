from flask import render_template
from . import main
from flask_login import login_required

#This defines the various views in our app
@main.route('/')
def index():
   """
   This function returns the index page and should fetch the pitches by category from the db.
   """
   #function for fetching the pitches from the db.
   
   return render_template('index.html')

@main.route('/pitch/')
def pitch():
   """
   Allow for more viewing of a given pitch.
   """
   #Should return a pitch by id
   render_template('pitch.html')