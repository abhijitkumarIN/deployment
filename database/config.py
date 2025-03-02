from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str 
    MAIL_USERNAME: str
    class Config:
        env_file = ".env"

settings = Settings()