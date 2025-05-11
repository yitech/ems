from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Market Data"
    api_version: str = "v1"
    websocket_url: str = "/ws/market-data"
    rest_api_url: str = "/api/market-data"
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()