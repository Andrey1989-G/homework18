# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение
from flask_restx import Api, resource
from config import Config
from flask import Flask

from flask_hard_blank.setup_db import db
from flask_hard_blank.views.directors import director_ns
from flask_hard_blank.views.genres import genre_ns
from flask_hard_blank.views.movies import movie_ns


def create_app(config: Config):
    # создаем приложение
    application = Flask(__name__)
    # задаем конфигурацию, через специальный метод
    application.config.from_object(config)
    # применение конфы которую мы настроили
    application.app_context().push()



def config_app(application):
    # метод для запуска сессии обращения к БД???
    db.init_app(application)
    #
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)



if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    config_app(app)
    app.run()
