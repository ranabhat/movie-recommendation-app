from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field
from movie.domain.genre import Genre


class MovieBase(BaseModel):
    id: Optional[UUID] = Field(..., description="uuid for a movie", example="7db5acd6-a0f0-44d9-8e15-d63414078a20")
    name: Optional[str] = Field(..., description="name of the movie", example="Zodiac")

class Movie(MovieBase):
    genre: Optional[List[Genre]] = None

# class MovieReturn(BaseModel):
#     moviesRecommendation: Optional[List[MovieBase]]
#     class Config:
#         schema_extra = {
#             "example": {
#                 "moviesRecommendation": [
#                     {
#                         "name": "Don't Look Up"
#                     }
#                 ]
#             }
#         }



