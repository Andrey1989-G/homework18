from flask_hard_blank.dao.movie_dao import MovieDao

class MovieService:
    """
    класс сервисов для MovieDao, построенный на crud
    """
    def __int__(self, dao: MovieDao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def get_movie_all_director(self, data):
        """
        получаем все фильмы режиссера
        :param data: получаем фамилию режиссера
        :return:
        """
        res = []
        for i in self.get_all():
            if i['director_id'] == data:
                res.append(i['title'])
        return res

    def get_movie_all_genre(self, data):
        """
        получаем все фильмы по жанру
        :param data: название жанра
        :return: список с фильмами одного жанра
        """
        res = []
        for i in self.get_all():
            if i['genre_id'] == int(data):
                res.append(i['title'])
        return res

    def get_movie_all_year(self, data):
        """
        получаем все фильмы по жанру
        :param data: название жанра
        :return: список с фильмами одного жанра
        """
        res = []
        for i in self.get_all():
            if i['genre_id'] == int(data):
                res.append(i['title'])
        return res

    def create(self, data):
        return self.dao.create(data)

    def movie_refactor(self, data):
        """
        меняем данные о фильме
        :param data: получаем данные, которые надо изменить
        :return: вызываем замену
        """
        mid = data.get('id')
        movie = self.get_one(mid)
        #обновляем данные
        #хочется схалтурить и задать обязательную замену полей
        #return {**movie, **data}
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        #вызываем замену
        self.dao.movie_refactor(movie)

    def movie_del(self, mid):
        return self.dao.movie_del(mid)
