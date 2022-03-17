from unittest import mock

from movie.domain.movie import Movie
from movie.domain.genre import Genre


movie_dict = {
        "id": "6fe6c94c-9796-4601-8ce9-ee95d40b0224",
        "name": "Dune",
        "genre": ["Sci-Fi"]   
}

movies = [Movie.from_dict(movie_dict)]

@mock.patch("app.api.api_v1.endpoints.movies.movie_list_use_case")
def test_get_all_movies(mock_use_case,client):
        mock_use_case.return_value = movies
        http_response = client.get("/api/v1/movies")
        assert http_response.json() == [movie_dict]
        mock_use_case.assert_called()
        assert http_response.status_code == 200

@mock.patch("app.api.api_v1.endpoints.movies.movie_recommended_use_case")
def test_get_recommended_movies_when_exist(mock_use_case, client):
        mock_use_case.return_value = movies
        http_response = client.get(f"/api/v1/movies/Sci-Fi")
        print(http_response.json())
        assert http_response.json() == [movie_dict]
        mock_use_case.assert_called()
        assert http_response.status_code == 200

@mock.patch("app.api.api_v1.endpoints.movies.movie_recommended_use_case")
def test_get_recommended_movies_when_not_exist(mock_use_case, client):
        mock_use_case.return_value = []
        http_response = client.get(f"/api/v1/movies/Film-Noir")
        detail=f"Recommendation for movies not found for genre:{Genre.FilmNoir.value}"
        assert http_response.json() == { "detail": detail }
        mock_use_case.assert_called()
        assert http_response.status_code == 404



