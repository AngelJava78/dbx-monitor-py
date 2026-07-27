import pandas as pd

from src.dbx_monitor.database.connection import get_engine
from src.dbx_monitor.database.queries import load_sql


def get_test_scenarios() -> pd.DataFrame:
    engine = get_engine()
    query = load_sql("select_test_scenarios.sql")

    return pd.read_sql(query, engine)