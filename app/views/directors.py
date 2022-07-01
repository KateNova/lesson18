from flask_restx import Resource, Namespace

from app.dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

# создаем экземпляры класса DirectorSchema
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsViews(Resource):

    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:did>')
class DirectorViews(Resource):

    def get(self, did):
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception as e:
            return "", 404
