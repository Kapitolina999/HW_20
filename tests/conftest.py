from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_1 = Director(id=1, name='Тейлор Шеридан')
    director_2 = Director(id=2, name='Квентин Тарантино')
    director_3 = Director(id=3, name='Владимир Вайншток')

    director_dao = DirectorDAO(None)
    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2])
    director_dao.create = MagicMock(return_value=director_3)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_1 = Genre(id=1, name='Ужас')
    genre_2 = Genre(id=2, name='Комедия')
    genre_3 = Genre(id=3, name='Драма')

    genre_dao = GenreDAO(None)
    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2])
    genre_dao.create = MagicMock(return_value=genre_3)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_1 = Movie(id=1, title='Йеллоустоун', description='Владелец ранчо пытается сохранить землю своих предков.',
                    trailer='https://www.youtube.com/watch?v=UKei_d0cbP4', year=2018, rating=8.6, genre_id=17,
                    director_id=1)
    movie_2 = Movie(id=20, title='Упс... Приплыли!', description='От Великого потопа зверей спас ковчег. '
                                                                 'Но спустя полгода скитаний они готовы сбежать с него '
                                                                 'куда угодно. Нервы на пределе. Хищники готовы забыть '
                    , trailer='https://www.youtube.com/watch?v=Qjpmysz4x-4', year=2020, rating=5.9, genre_id=16,
                    director_id=19)
    movie_3 = Movie(id=14, title='Лето',
                    description='Рассказ о начале творческого пути Виктора Цоя и группы «Кино», о его взаимоотношениях'
                                'с Майком Науменко, его женой Натальей и многими, кто был в авангарде рок-движения '
                                'Ленинграда 1981 года.', trailer='https://www.youtube.com/watch?v=TvAbtsQKrHA',
                    year=2018, rating=7.3, genre_id=4, director_id=12)

    movie_dao = MovieDAO(None)
    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2])
    movie_dao.create = MagicMock(return_value=movie_3)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
