from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODEL_NAME: str
    API_KEY: str
    BASE_URL: str

    TEMPERATURE: float=0.5
    MAX_TOKENS: int=4096
    REQUEST_TIMEOUT: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()