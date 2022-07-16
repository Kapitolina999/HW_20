import pytest

from service.movie import MovieService


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_data = {'id': 14, 'title': 'ЛетоНовое',
                      'description': 'Рассказ о начале творческого пути Виктора Цоя и группы «Кино», о его '
                                    'взаимоотношениях с Майком Науменко, его женой Натальей и многими, кто был в '
                                    'авангарде рок-движения Ленинграда 1981 года.',
                      'trailer': 'https://www.youtube.com/watch?v:TvAbtsQKrHA',
                      'year': 2018,
                      'rating': 7.3,
                      'genre_id': 4,
                      'director_id': 12}
        movie = self.movie_service.create(movie_data)
        assert movie.id is not None

    def test_update(self):
        movie_data = {'id': 14, 'title': 'ЛетоНовое',
                      'description': 'Рассказ о начале творческого пути Виктора Цоя и группы «Кино», о его '
                                    'взаимоотношениях с Майком Науменко, его женой Натальей и многими, кто был в '
                                    'авангарде рок-движения Ленинграда 1981 года.',
                      'trailer': 'https://www.youtube.com/watch?v:TvAbtsQKrHA',
                      'year': 2018, 'rating': 7.3, 'genre_id': 4, 'director_id': 12}
        movie = self.movie_service.update(movie_data)
        assert movie.id is not None

    def test_delete(self):
        movie = self.movie_service.delete(3)
        assert movie is None
