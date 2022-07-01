from app.dao.model.director import Director


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, director_id):
        return self.session.query(Director).filter(Director.id == director_id).one()

    def get_all(self):
        return self.session.query(Director).all()
