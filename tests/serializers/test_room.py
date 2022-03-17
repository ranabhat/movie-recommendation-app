import json
import uuid

from movie.serializers.movie import MovieJsonEncoder
from movie.domain.movie import Movie

def test_serialize_domain_movie():
    id = uuid.uuid4()

    movie = Movie(
        id,
        name="Zodiac",
        genre=["Crime", "Thriller"]
    )

    # the double curly braces are used to avoid clashes with the f-string formatter)
    expected_json = f"""
        {{
            "id": "{id}",
            "name": "Zodiac",
            "genre": ["Crime", "Thriller"]
        }}
    
    """

    json_movie = json.dumps(movie, cls=MovieJsonEncoder)
    assert json.loads(json_movie) == json.loads(expected_json)
