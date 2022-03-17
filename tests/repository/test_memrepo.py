import pytest

from movie.domain.movie import Movie
from movie.repository.memrepo import MemRepo

@pytest.fixture
def movie_dicts():
    return [
        {
            "id": "23312d0b-ca4d-44fc-995c-d820428b9b76",
            "name": "Dune",
            "genre": ["Sci-Fi"]
        },
        {
            "id": "d52ede5f-e94e-4eeb-ae63-29a50b126e16",
            "name": "Notebook",
            "genre": ["Romance"]
        },
        {
            "id": "41b24b2b-c0dc-4790-8935-c0cd531fc332",
            "name": "Prisoners",
            "genre": ["Crime", "Thriller"]
        },
        {
            "id": "0523974c-5ec1-44e0-a6d5-6bc65811554d",
            "name": "14 Peaks",
            "genre": ["Documentary"]
        },
        {
            "id": "e73c6138-81fb-4ed0-9655-4afc3a0118f9",
            "name": "Don't Look Up",
            "genre": ["Comedy"]
        },
        {
            "id": "7db5acd6-a0f0-44d9-8e15-d63414078a20",
            "name": "Zodiac",
            "genre": ["Thriller"]
        }    
    ]

@pytest.fixture
def empty_movie_dicts():

    return []

def test_repository_list_without_parameters(movie_dicts):
    repo = MemRepo(movie_dicts)

    movies = [Movie.from_dict(i) for i in movie_dicts]

    assert repo.list() == movies

@pytest.mark.parametrize('genre', [
    ('Thriller'),
    ('Comedy'),
    ('Horror'),
    ('Sci-Fi'),
    (None)
])
def test_repository_recommended_list_with_parameters(movie_dicts, genre):
    repo = MemRepo(movie_dicts, genre)
    recommended_movies = [Movie.from_dict(movie) for movie in movie_dicts if genre in movie["genre"]]
    assert repo.recommended_list() == recommended_movies

@pytest.mark.parametrize('genre', [
    ('Thriller'),
    ('Comedy'),
    ('Horror'),
    ('Sci-Fi'),
    (None)
])
def test_repository_recommended_list_without_parameters(empty_movie_dicts, genre):
    repo = MemRepo(empty_movie_dicts, genre)
    recommended_movies = [Movie.from_dict(movie) for movie in empty_movie_dicts if genre in movie["genre"]]
    assert repo.recommended_list() == recommended_movies
    