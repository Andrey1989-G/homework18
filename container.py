from flask_hard_blank.dao.director_dao import DirectorDao
from flask_hard_blank.dao.genre_dao import GenreDao
from flask_hard_blank.dao.movie_dao import MovieDao
from flask_hard_blank.service.movie_serv import MovieService
from setup_db import db

director_dao = DirectorDao(db.session)

genre_dao = GenreDao(db.session)

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)