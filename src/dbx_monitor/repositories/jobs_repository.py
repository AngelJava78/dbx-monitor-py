import pandas as pd

from src.dbx_monitor.database.connection import get_engine
from src.dbx_monitor.database.queries import load_sql


def get_jobs() -> pd.DataFrame:
    engine = get_engine()
    query = load_sql("select_jobs.sql")

    df = pd.read_sql(query, engine)

    df["started_cdmx"] = pd.to_datetime(df["started_cdmx"], errors="coerce")
    df["ended_cdmx"] = pd.to_datetime(df["ended_cdmx"], errors="coerce")

    return df
