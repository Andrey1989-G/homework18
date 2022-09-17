from model.director_model import Director
#crud

class DirectorDao:
    """
    в этом классе:
    Получаем режиссера по id
    Получаем всех режиссеров
    Принимаем открытую сессию(db) в базу данных
    """
    def __int__(self, session):
        self.session = session

    def get_one(self, did):
        """
        Получить режиссера по id
        :param did: id режиссера
        :return:
        """
        return self.session.query(Director).get(did)

    def get_all(self):
        """
        Получаем всех режиссеров
        :return:
        """
        return self.session.query(Director).get(all)

