from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings configuration class.
    Contains all configuration parameters for the API.
    """
    # Project configuration
    PROJECT_NAME: str = "Demo API"
    PROJECT_DESCRIPTION: str = "Una API de demostración con FastAPI"
    PROJECT_VERSION: str = "0.1.0"
    
    # Server configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True

    # CORS configuration
    CORS_ORIGINS: list[str] = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ["*"]
    CORS_ALLOW_HEADERS: list[str] = ["*"]
    
    class Config:
        """
        Configuration for the Settings class.
        Defines environment file settings and behavior.
        """
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings() 