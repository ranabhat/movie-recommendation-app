import pytest
import uuid
from unittest import mock

from movie.domain.movie import Movie
from movie.use_cases.movie_recommended_list import movie_recommended_use_case

@pytest.fixture
def recommended_movies():

    movie_1 = Movie(
         id=uuid.uuid4(),
         name="Prisoners",
         genre=["Crime", "Thriller"]
    )
    
    movie_2 = Movie(
         id=uuid.uuid4(),
         name="Zodiac",
         genre=["Thriller"]
    )

    return [movie_1, movie_2]

def test_movie_recommendation(recommended_movies):
     repo = mock.Mock()
     repo.recommended_list.return_value = recommended_movies

     result = movie_recommended_use_case(repo)

     repo.recommended_list.assert_called_with()
     assert result == recommended_movies