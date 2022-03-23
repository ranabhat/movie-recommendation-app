import pytest
import uuid
from unittest import mock

from movie.domain.movie import Movie
from movie.use_cases.movie_list import MovieRecommendationUsecase


@pytest.fixture
def domain_movies():

    movie_1 = Movie(
         id=uuid.uuid4(),
         name="Dune",
         genre=["Sci-Fi"]
    )
    
    movie_2 = Movie(
         id=uuid.uuid4(),
         name="Notebook",
         genre=["Romance"]
    )
    movie_3 = Movie(
         id=uuid.uuid4(),
         name="Prisoners",
         genre=["Crime", "Thriller"]
    )

    movie_4 = Movie(
         id=uuid.uuid4(),
         name="14 Peaks",
         genre=["Documentary"]
    )

    movie_5 = Movie(
         id=uuid.uuid4(),
         name="Don't Look Up",
         genre=["Comedy"]
    )

    movie_6 = Movie(
         id=uuid.uuid4(),
         name="Zodiac",
         genre=["Thriller"]
    )

    return [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6]

def test_movie_list_without_parameters(domain_movies):
    repo = mock.Mock()
    repo.list.return_value = domain_movies

    result = MovieRecommendationUsecase(repo).movie_list_use_case()

    repo.list.assert_called_with()
    assert result == domain_movies




