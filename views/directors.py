from flask_restx import Api, Resource, Namespace

from flask_hard_blank.container import director_dao
from flask_hard_blank.dao.model.director_model import DirectorSchema


# Единичная сериализация
director_schema = DirectorSchema()

# Множественная сериализация
directors_schema = DirectorSchema(many=True)


director_ns = Namespace('directors')

@director_ns.route('/')
class DirectorsView(Resource):
    def page_all_directors(self):
        res = director_dao.get_all()
        return res, 200


@director_ns.route('/<int:did>')
class DirectorsView(Resource):
    def page_all_directors(self, did):
        res = director_dao.get_one(did)
        return res, 200

