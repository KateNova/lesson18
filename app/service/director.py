from app.dao.director import DirectorDAO


class DirectorService():
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, director_id):
        return self.dao.get_one(director_id)

    def get_all(self):
        return self.dao.get_all()
