from flask import Blueprint, jsonify, request
from . import db
from .models import Movie
from flask_cors import CORS

main = Blueprint('main', __name__)
CORS(main, supports_credentials=True)

@main.route('/add_movie', methods=['POST'])
def add_movie():
	movie_data = request.get_json()

	new_movie = Movie(id=movie_data['id'],title=movie_data['title'], rating=movie_data['rating'], image=movie_data['image'], description=movie_data['description'])

	db.session.add(new_movie)
	db.session.commit()

	return 'Done', 201

@main.route('/movies')
def movies():
	movie_list = Movie.query.all()
	movies = []
	
	for movie in movie_list:
		movies.append({'id':movie.id,'title' : movie.title, 'rating' : movie.rating, 'image' : movie.image, 'description' : movie.description})

	return jsonify ({'movies': movies})

