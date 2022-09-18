from flask_hard_blank.dao.director_dao import DirectorDao
from flask_hard_blank.dao.genre_dao import GenreDao
from flask_hard_blank.dao.movie_dao import MovieDAO
from flask_hard_blank.service.movie_serv import MovieService
from setup_db import db

sess=db.session

director_dao = DirectorDao(sess)

genre_dao = GenreDao()

movie_dao = MovieDAO(sess)
movie_service = MovieService(movie_dao)