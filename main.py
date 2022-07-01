from flask import Flask

# функция создания основного объекта app
from flask_restx import Api

from app.config import Config
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from setup_db import db


def create_app(config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run()
