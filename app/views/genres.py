from flask_restx import Resource, Namespace

from app.dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

# создаем экземпляры класса GenreSchema
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresViews(Resource):

    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:gid>')
class GenreViews(Resource):

    def get(self, gid):
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return "", 404
