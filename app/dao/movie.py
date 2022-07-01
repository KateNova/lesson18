from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, movie_id):
        return self.session.query(Movie).filter(Movie.id == movie_id).one()

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id)

    def get_by_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id)

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def update(self, movie_by_id):
        self.session.add(movie_by_id)
        self.session.commit()
        return movie_by_id

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie_id):
        movie_by_id = self.session.query(Movie).filter(Movie.id == movie_id).one()
        self.session.delete(movie_by_id)
        self.session.commit()
