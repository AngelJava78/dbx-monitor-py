import pandas as pd

from src.dbx_monitor.database.connection import get_engine
from src.dbx_monitor.database.queries import load_sql

def get_state_list() -> list[str]:
    engine = get_engine()
    query = load_sql("select_states.sql")
    df = pd.read_sql(query, engine)
    return df["result_state"].dropna().astype(str).tolist()
