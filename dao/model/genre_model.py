from marshmallow import Schema, fields
from flask_hard_blank.setup_db import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


# наполняем бд
# genre = Genre(id=1, name='novell')
# GenreSchema.dumps(genre)

# Единичная сериализация
genre_schema = GenreSchema()
# Множественная сериализация
genres_schema = GenreSchema(many=True)
