#initial route setup stuff:
from app import app
from flask import render_template


#this is for my variable behavior in aboutmarvel html
from random import choice

#this is my import for the form i created
from .forms import CharacterForm
#we can now use this form in any of our routes

#request post so that we can use the request method with our routes
from flask import request
#import requests as r

@app.route('/')
@app.route('/marvelhomepage') #decorator says this is a route of the flask app 'app' with the url endpoint '/marvelhomepage'
def home():
    headline= 'HELLO MARVEL FANS, WELCOME TO THE MARVEL HOMEPAGE'
    favorites = ['GREEN GOBLIN','MAGNETO', 'RED SKULL', 'LOKI']
    return render_template('index.html', headline=headline, favorites=favorites)

@app.route('/aboutmarvel')
def aboutmarvel():
    headline= 'THIS IS ABOUT THE HISTORY OF MARVEL'
    x= choice(['WELCOME FANS', 'THANKS FOR VISITING', 'WE APPRECIATE YOUR LOYAL SUPPORT'])
    return render_template('aboutmarvel.html',headline=headline, greetings=x )

