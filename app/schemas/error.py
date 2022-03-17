from pydantic import BaseModel, Field

class ResourceNotFoundError(BaseModel):
    detail: str = Field(..., description="Error Message Description")
    class Config:
        schema_extra = {
            "example": {
                "detail": "Recommendation for movies not found for genre: <unavailable genre>"
            }
        }