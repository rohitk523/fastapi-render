from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_KEY: str = "your-default-api-key"
    
    class Config:
        env_file = ".env"

settings = Settings()