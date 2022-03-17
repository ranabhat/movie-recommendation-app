import uuid
from movie.domain.movie import Movie

def test_movie_model_init():
    id = uuid.uuid4() 
    movie = Movie(
        id,
        name="Zodiac",
        genre=["Crime", "Thriller"]
    )
    assert movie.id == id
    assert movie.name == "Zodiac"
    assert movie.genre == ["Crime", "Thriller"]

def test_movie_model_from_dict():
    id = uuid.uuid4() 
    init_dict = {
        "id": id,
        "name": "Zodiac",
        "genre": ["Crime", "Thriller"]
    }

    movie = Movie.from_dict(init_dict)

    assert movie.id == id
    assert movie.name == "Zodiac"
    assert movie.genre == ["Crime", "Thriller"]

def test_movie_model_to_dict():
    init_dict = {
        "id": uuid.uuid4(),
        "name": "Zodiac",
        "genre": ["Crime", "Thriller"]
    }
    movie = Movie.from_dict(init_dict)
    assert movie.to_dict() == init_dict