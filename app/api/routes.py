#intial blueprint setup
from flask import Blueprint, jsonify, request
#instantiate blueprint api and then create a connection between the blueprint api and my flask app.
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/test')
def test():
    #jsonify? transorms python dictionary (or list) into json data, must import jsonify next to blueprints to use
    return jsonify({'database': 'whoa this is some cool data'}), 200



#route for getting all characters
@api.route('/movies', methods=['GET'])
def getCharacter():
     """
     [Get] return json data on all of the characters in our database
     """
#     #query the movies
#     #I want to jsonify the result of .to_dict() for each movie in our movies query
#     movies = [m.to_dict() for m in Movies.query.all()]
#     #jsonify and send
#     return jsonify(movies)
