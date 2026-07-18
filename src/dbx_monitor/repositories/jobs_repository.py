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

def get_jobs_by_folio_number(folio_number: str) -> pd.DataFrame:
    engine = get_engine()
    query = load_sql("select_jobs_by_folio.sql")
    params = {
        "folio_number": f"%{str(folio_number).strip()}%",
    }
    df = pd.read_sql(query, engine, params=params)
    df["started_cdmx"] = pd.to_datetime(df["started_cdmx"], errors="coerce")
    df["ended_cdmx"] = pd.to_datetime(df["ended_cdmx"], errors="coerce")    
    return df

def get_jobs_by_range_of_date(start_date, end_date) -> pd.DataFrame:
    if not start_date or not end_date:
        return pd.DataFrame()    
    engine = get_engine()
    query = load_sql("select_jobs_by_range_of_date.sql")
    params = {
        "start_date": start_date,
        "end_date": end_date,
    }
    df = pd.read_sql(query, engine, params=params)
    df["started_cdmx"] = pd.to_datetime(df["started_cdmx"], errors="coerce")
    df["ended_cdmx"] = pd.to_datetime(df["ended_cdmx"], errors="coerce")    
    return df