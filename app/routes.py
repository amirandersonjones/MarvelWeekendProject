#initial route setup stuff:
from app import app
from flask import render_template

@app.route('/')
@app.route('/marvelhomepage') #decorator says this is a route of the flask app 'app' with the url endpoint '/marvelhomepage'
def home():
    return render_template('index.html')

@app.route('/aboutmarvel')
def aboutmarvel():
    return render_template('aboutmarvel.html')
