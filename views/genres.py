import flask
from flask_restx import Api, Resource, Namespace

from flask_hard_blank.container import genre_dao
from flask_hard_blank.dao.model.genre_model import GenreSchema

# Единичная сериализация
genre_schema = GenreSchema()

# Множественная сериализация
genres_schema = GenreSchema(many=True)

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        res = genre_dao.get_all()
        return genres_schema.dump(res), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        res = genre_dao.get_one(gid)
        return genre_schema.dump(res), 200
