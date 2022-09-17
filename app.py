# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение
from flask_restx import Api, resource
from flask import Flask

from flask_hard_blank.views.directors import director_ns

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
api.add_namespace(director_ns)


if __name__ == '__main__':
    app.run(debug=True)
