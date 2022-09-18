import flask
from flask_restx import Api, Resource, Namespace

from flask_hard_blank.container import movie_service
from flask_hard_blank.dao.model.movie_model import MovieSchema



# Единичная сериализация
movie_schema = MovieSchema()

# Множественная сериализация
movies_schema = MovieSchema(many=True)

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        args = flask.request.args
        return movies_schema.dump(movie_service.get_all(args)), 200
    def post(self):
        if movie_service.create(flask.request.args):
            return '', 200


@movie_ns.route('/<int:mid>')
class MoviesViews(Resource):
    def get(self, mid):
        res = movie_service.get_one(mid)
        return movies_schema.dump(res), 200
    def put(self):
        if movie_service.movie_refactor(flask.request.args):
            return '', 200
    def delete(self, mid):
        if movie_service.movie_del(mid):
            return '', 200


