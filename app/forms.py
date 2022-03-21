#THIS PAGE IS FOR LAYING OUT OBJECTS FOR EACH OF OUR FORMS
#THESE OBJECTS WILL DESCRIBE THE FORMS FIELDS, TYPES OF DATA, AND ANY VALIDATORS

#IMPORTS
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#class for the form describing the form's structure and datatype
#2 fields for this form asking for driver or whatever and a submit button
#this custom class inherits from FlaskForm it is our customization of the baseform structure froom flask wtf
class CharacterForm(FlaskForm):
    #having done the inheritence we just need to provide the fields that this form will show
    charactername = StringField('Character Name', validators=[DataRequired()]) #driver name in parenthesis 
    #is the label for the field. the DataRequired means we don't allow someone to 
    # submit the form without typing a drive in 
    submit = SubmitField()