from flask_hard_blank.dao.model.genre_model import Genre

#crud но без ud

class GenreDao:
    """
    в этом классе возвращаем
    один жанр по id
    все жанры
    принимаем открытую сессию к бд
    """
    def __int__(self, session):
        self.session = session

    def get_one(self, gid):
        """
        возвращаем жанр по айди
        :param gid: id -> int
        :return:
        """
        return self.session.query(Genre).get(gid)

    def get_all(self):
        """
        возвращаем все жанры
        :return:
        """
        return self.session.query(Genre).get(all)
