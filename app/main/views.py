from flask import render_template
from . import main
from flask_login import login_required
from .. import db
from ..models import Pitch

#This defines the various views in our app
@main.route('/')
def index():
   """
   This function returns the index page and should fetch the pitches by category from the db.
   """
   #function for fetching the pitches from the db.
   pitches = Pitch.query.all()
   print(pitches)
   return render_template('index.html', pitches = pitches) 

@main.route('/pitch/<int:id>')
def pitch(id):
   """
   Allow for more viewing of a given pitch.
   """
   #Should return a pitch by id   
   return render_template('pitch.html', id = id)