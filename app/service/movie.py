from app.dao.movie import MovieDAO


class MovieService():
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, movie_id):
        return self.dao.get_one(movie_id)

    def get_all(self):
        return self.dao.get_all()

    def get_by_director(self, director_id):
        return self.dao.get_by_director(director_id)

    def get_by_genre(self, genre_id):
        return self.dao.get_by_genre(genre_id)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def update(self, movie_id, data):
        movie_by_id = self.dao.get_one(movie_id)
        for k, v in data.items():
            setattr(movie_by_id, k, v)
        return self.dao.update(movie_by_id)

    def create(self, data):
        return self.dao.create(data)

    def delete(self, movie_id):
        self.dao.delete(movie_id)
