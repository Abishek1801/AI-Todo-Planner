from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    
    #app enviornment 
    app_env: str
    #app port
    app_port: int

    #secret key 
    secret_key: str

    # ── PostgreSQL ───
    postgres_user: str
    postgres_password: str
    postgres_db: str
    # Assembled from the values above — change only if you rename the service
    database_url: str


    # ── Neo4j ──
    neo4j_uri: str
    neo4j_user: str
    neo4j_password: str


    # ── ChromaDB ──────────────────────────────
    # Service name in docker-compose is "chroma"
    chroma_host: str
    chroma_port: int


    # ── Redis ─────────────────────────────────
    # Service name in docker-compose is "redis"
    redis_url: str


    # ── Anthropic (Claude) ────────────────────
    # Get your key from: https://console.anthropic.com
    anthropic_api_key: str


    # ── Google OAuth ──────────────────────────
    # Create credentials at: https://console.cloud.google.com
    # Application type: Web application
    # You will need Gmail API and Google Calendar API enabled
    google_client_id: str
    google_client_secret: str

    # This must match exactly what you set in Google Cloud Console
    google_redirect_uri: str


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
