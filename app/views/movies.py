from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.movie import MovieSchema
from implemented import movie_service

# создаем нэймспейс для представления
movie_ns = Namespace('movies')

# создаем экземпляры класса MovieSchema
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


# делаем Class Based Views
@movie_ns.route('/')
class MoviesViews(Resource):

    def get(self):
        # добавляем фильтры
        if request.args.get('director_id', None):
            all_movies = movie_service.get_by_director(request.args['director_id'])
        elif request.args.get('genre_id', None):
            all_movies = movie_service.get_by_genre(request.args['genre_id'])
        elif request.args.get('year', None):
            all_movies = movie_service.get_by_year(request.args['year'])
        else:
            all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        request_movie = request.json
        movie = movie_service.create(request_movie)
        return "", 201, {"Location": f'/movies/{movie.id}'}


@movie_ns.route('/<int:mid>')
class MovieViews(Resource):

    def get(self, mid):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return "", 404

    def put(self, mid):
        try:
            movie_service.update(mid, request.json)
            return "movie updated successfully", 200
        except Exception as e:
            return e.__str__(), 500

    def delete(self, mid):
        try:
            movie_service.delete(mid)
            return "movie deleted successfully", 204
        except Exception as e:
            return e.__str__(), 500
