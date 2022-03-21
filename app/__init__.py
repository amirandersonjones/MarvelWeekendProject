
#initial flask setup stuff:
from flask import Flask
# from our config file import the Config class that we created
from config import Config

# define/instantiate our Flask object... aka tell the computer that this is a flask app
app = Flask(__name__)

# tell this app how it should be configured - over to the config.py file to set up for this!
app.config.from_object(Config)
# aka configure our flask app from the Config object we just wrote

# our flask app is dumb! we need to tell it if any routes or models exist!
# import the routes file here (must be after the definition and config of app)
from . import routes # from the app folder (that we're currently in) import the routes file
#end intial setup stuff

#imports for database intial setup stuff:
from .models import db
from flask_migrate import Migrate

#set up our ORM and Migrate connections
db.init_app(app)
migrate = Migrate(app, db)
from . import models # from the app folder import the models file. this MUST come after the setup steps

# import blueprints
from .api.routes import api

#create a link of communication between blueprints and app
#aka register the blueprints
app.register_blueprint(api)