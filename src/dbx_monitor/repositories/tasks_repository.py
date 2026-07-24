import pandas as pd
import logging

from src.dbx_monitor.database.connection import get_engine
from src.dbx_monitor.database.queries import load_sql


def get_tasks_by_run_id(run_id: int) -> pd.DataFrame:
    logging.info(
        "Fetching tasks for run_id=%s",
        run_id,
    )
    try:

        engine = get_engine()
        query = load_sql("select_tasks.sql")
        logging.info("")

        params = {"run_id": run_id}
        df = pd.read_sql(query, engine, params=params)
        df["started_cdmx"] = pd.to_datetime(df["started_cdmx"], errors="coerce")
        df["ended_cdmx"] = pd.to_datetime(df["ended_cdmx"], errors="coerce")  
        logging.info(
            "Task query completed for run_id=%s. Records found=%s",
            run_id,
            len(df),
        )
        return df
    except Exception:
        logging.exception(
            "Failed to fetch tasks for run_id=%s",
            run_id,
        )
        raise
