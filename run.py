#the purpose of this file is to give my terminal and flask shell access to components 
# of my app to test through my CLI(not worrying about templates or routes)

#when u want to do testing through the flask shell with this context processor 
#change your FLASK_APP variable in .env to run.py

from app import app
from app.models import db, User

#shell context processor-gives y flask shell ( a little terminal that has access to my flask app) 
# access to my database models, etc.
@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User}