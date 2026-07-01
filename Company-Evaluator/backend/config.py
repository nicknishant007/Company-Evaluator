from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Company Evaluator API"

    VERSION: str = "1.0.0"

    API_PREFIX: str = "/api/v1"

    DEBUG: bool = True


settings = Settings()