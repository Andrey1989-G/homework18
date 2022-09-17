from model.movie_model import Movie


#crud


class MovieDao:
    def __int__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).get(all)

    def get_movie_all_director(self, movies):
        """
        возвращаем все фильмы режиссера
        :param movies: список с фильмами одного режиссера
        :return: список с фильмами одного режиссера
        """
        return movies

    def get_movie_all_genre(self, movies):
        """
        возвращаем все фильмы по жанру
        :param movies: список с фильмами одного жанра
        :return: список с фильмами одного жанра
        """
        return movies

    def get_movie_all_year(self, movies):
        """
        возвращаем все фильмы за год
        :param movies: список с фильмами за год
        :return: список с фильмами за год
        """
        return movies

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def movie_refactor(self, movie):
        self.session.add(movie)
        self.session.commit

    def movie_del(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()