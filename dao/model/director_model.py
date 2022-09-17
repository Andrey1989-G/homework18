from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
from flask_hard_blank.setup_db import db

class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()

# в джейсон, пора бы уже запомнить, блин, что с "s"!!!!!!!
# наполняем бд
# director = Director(id=1, name='Kusturica')
# DirectorSchema.dumps(director)
