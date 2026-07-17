from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from src.dbx_monitor.config.settings import get_settings


def get_engine() -> Engine:
    settings = get_settings()

    connection_url = (
        "postgresql+psycopg2://"
        f"{settings.postgres_user}:{settings.postgres_password}"
        f"@{settings.postgres_host}:{settings.postgres_port}"
        f"/{settings.postgres_database}"
    )

    return create_engine(connection_url)
