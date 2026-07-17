from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    postgres_host: str
    postgres_port: str
    postgres_database: str
    postgres_user: str
    postgres_password: str


def get_settings() -> Settings:
    return Settings(
        postgres_host=os.getenv("POSTGRES_HOST", ""),
        postgres_port=os.getenv("POSTGRES_PORT", "5432"),
        postgres_database=os.getenv("POSTGRES_DATABASE", ""),
        postgres_user=os.getenv("POSTGRES_USER", ""),
        postgres_password=os.getenv("POSTGRES_PASSWORD", ""),
    )
