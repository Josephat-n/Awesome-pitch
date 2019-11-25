from flask import render_template
from . import main


#This defines the various views in our app
@main.route('/')
def index():
   """
   This function returns the index page and should fetch the pitches by category from the db.
   """
   #function for fetching the pitches from the db.
   
   return render_template('index.html')
