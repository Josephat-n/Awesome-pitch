from flask import render_template
from . import main
from flask_login import login_required, current_user
from .. import db
from ..models import Pitch
from .forms import CommentForm

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
   a_pitch = Pitch.query.filter_by(id= id)
   print(a_pitch)
   return render_template('pitch.html', id = id, a_pitch = a_pitch)

@main.route('/pitch/comment/<int:id>', methods = ['GET','POST'])
@login_required
def comment(id):
   """
   Write a comment on any pitch
   """
   form = CommentForm()
   return render_template('comment.html',id = id, comment_form=form)