#this models.py file is responsible for everything database
#primarily the instantiation of our ORM adn the creation of our database models(aka tables/entities)

#intial setup stuff:
#import our ORM
from flask_sqlalchemy import SQLAlchemy
#create the instance of our ORM(object relational mapper aka translator between python and SQL)
db = SQLAlchemy()

#extra imports to work with our tables we create:
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4 #the standard normal id a fuction is generated here so we have to string it in our init method
from secrets import token_hex

class User(db.Model):
    #lay out our columns liek we would in a SQL create table query
    id = db.Column(db.String(50), primary_key=True) #primary key makes this automatically not nullable as well as unique
    username = db.Column(db.String(15), nullable=False, unique=True)
    email= db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50)) #will be nullable and they don't have to be unique so we can leave this blank
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(250), nullable= False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc)) #have to import




#new DB model for our animals
class Character(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    descripton = db.Column(db.String(250))
    comics_appeared_in = db.Column(db.Integer)
    image = db.Column(db.String(150), nullable=True)
    super_power = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    price = db.Column(db.Float(2), nullable=False)

    def __init__(self, dict):
        """
        expected dict struture:
        {
            'name': <str>,
            'price': <float>,
            ###rest of k:v pairs optional
            'description': <str>,
            'comics_appeared_in': <str>
            'image': <str>
            'super_power':<str>
            'date_created':<timestamp>
        }
        """
        self.id = str(uuid4())
        self.name = dict['name'].title()
        self.price = dict['price']
        self.description = dict.get('description')
        self.image = dict.get('image') #storing an image in a sql database is not a good idea. no sql or a free image hosting site is a better idea.
        self.comics_appeared_in = dict.get('comics_appeared_in') #w/this if the key does't exist it will return none. if we used the normal bracket notation we would get an error
        self.super_power = dict.get('super_power')
    
    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description':self.description,
            'comics_appeared_in': self.comics_appeared_in,
            'super_power':self.super_power ,
            }
    
    
    def from_dict(self, dict):
        """
        works for the updateCharacter route-accepts the dictionary provided by the request and updates the animal with any present keys
        """
        if dict.get('name'):
            self.name = dict['name'].title()
        if dict.get('price'):
            self.price = dict['price']
        if dict.get('image'):
            self.image = dict['image']
        if dict.get('description'):
            self.description = dict['description']   
        if dict.get('comics_appeared_in'):
            self.size = dict['comics_appeared_in']
        if dict.get('super_power'):
            self.diet = dict['super_power']
        