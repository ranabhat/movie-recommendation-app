from fastapi import APIRouter, HTTPException, status
from typing import List, Any
from app import schemas
from movie.domain.genre import Genre
from movie.repository.memrepo import MemRepo
from movie.use_cases.movie_list import MovieRecommendationUsecase
#from movie.use_cases.movie_recommended_list import movie_recommended_use_case
from movie.serializers.movie import MovieJsonEncoder
import json

router = APIRouter()

movies = [
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

@router.get("/", response_model=List[schemas.Movie])
async def get_all_movies():
    repo = MemRepo(movies)
    result = MovieRecommendationUsecase(repo).movie_list_use_case()
    encode_to_json_string = json.dumps(result, cls=MovieJsonEncoder)
    return json.loads(encode_to_json_string)


@router.get("/{genre}", response_model=List[schemas.Movie], responses={status.HTTP_404_NOT_FOUND: {"model": schemas.ResourceNotFoundError}})
async def get_recommended_movies(
    genre: Genre
) -> Any:
    """
    Get movies by genre.
    """

    repo = MemRepo(movies, genre)
    result = MovieRecommendationUsecase(repo).movie_recommended_use_case()
    if not result:
        detail=f"Recommendation for movies not found for genre:{genre.value}"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
    encode_to_json_string = json.dumps(result, cls=MovieJsonEncoder)
    return json.loads(encode_to_json_string)
