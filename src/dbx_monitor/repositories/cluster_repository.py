import pandas as pd

from src.dbx_monitor.database.connection import get_engine
from src.dbx_monitor.database.queries import load_sql


def get_cluster_usage() -> pd.DataFrame:
    engine = get_engine()
    query = load_sql("select_cluster.sql")

    df = pd.read_sql(query, engine)
    df["start_time_cdmx"] = pd.to_datetime(df["start_time_cdmx"], errors="coerce")

    return df

def get_cluster_usage_by_range_of_date(start_date, end_date) -> pd.DataFrame:
    engine = get_engine()
    query = load_sql("select_cluster_by_range_of_date.sql")
    params = {
        "start_date": start_date,
        "end_date": end_date,
    }
    df = pd.read_sql(query, engine, params=params)
    df["start_time_cdmx"] = pd.to_datetime(df["start_time_cdmx"], errors="coerce")

    return df
