# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.
from flask import Flask

# Пример

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////data/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

