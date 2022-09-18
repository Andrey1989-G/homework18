from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from flask_hard_blank.setup_db import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    # делаем связь один ко многим.    \/здесь делаем внешний ключ('название таблицы.столбик')
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    director = db.relationship('Director')
    genre = db.relationship('Genre')


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()


# Единичная сериализация
movie_schema = MovieSchema()

# Множественная сериализация
movies_schema = MovieSchema(many=True)
