from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, genre_id):
        return self.session.query(Genre).filter(Genre.id == genre_id).one()

    def get_all(self):
        return self.session.query(Genre).all()
