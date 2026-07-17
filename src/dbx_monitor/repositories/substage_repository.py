from sqlalchemy import text
from src.dbx_monitor.database.connection import get_engine
from src.dbx_monitor.database.queries import load_sql
from src.dbx_monitor.models.substage import Substage

def get_substages() -> list[Substage]:
    engine = get_engine()
    query = load_sql("select_substages.sql")
    
    with engine.connect() as connection:
        result = connection.execute(text(query))

        return [
            Substage (
                substage_id= row.substage_id,
                substage_name = row.substage_name
            )
            for row in result
        ]