from sqlalchemy import text
from src.dbx_monitor.database.connection import get_engine
from src.dbx_monitor.database.queries import load_sql
from src.dbx_monitor.models.subprocess import Subprocess

def get_subprocesses() -> list[Subprocess]:
    engine = get_engine()
    query = load_sql("select_subprocesses.sql")

    with engine.connect() as connection:
        result = connection.execute(text(query))
        return [
            Subprocess(
                subprocess_id = row.subprocess_id,
                subprocess_name = row.subprocess_name
            )
            for row in result
        ]