# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.
from flask import Flask

# Пример

def create_app():
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

