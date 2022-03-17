from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Simple Movie Recommendation API"
    PROJECT_DESCRIPTION: str = "With this API, the user can get movie recommendation based on the genre."
    API_VERSION: str = "1.0.0"

    class Config:
        case_sensitive = True


settings = Settings()