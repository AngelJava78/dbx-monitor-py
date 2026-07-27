from datetime import datetime, timedelta

import pandas as pd

from src.dbx_monitor.database.connection import get_engine
from src.dbx_monitor.database.queries import load_sql


def get_volume_test_runs(
    start_date: str,
    end_date: str,
    scenario_id: int = 0,
    subprocess_id: int = 0,
    folio: str | None = None,
) -> pd.DataFrame:
    if not start_date or not end_date:
        return pd.DataFrame()

    parsed_start_date = pd.to_datetime(
        start_date,
        errors="raise",
    )

    parsed_end_date = pd.to_datetime(
        end_date,
        errors="raise",
    )

    if parsed_start_date >= parsed_end_date:
        raise ValueError("The start date must be earlier than the end date.")

    normalized_folio = None

    if folio and folio.strip():
        normalized_folio = f"%{folio.strip()}%"

    params = {
        "start_date": parsed_start_date.to_pydatetime(),
        "end_date": parsed_end_date.to_pydatetime(),
        "scenario_id": int(scenario_id or 0),
        "subprocess_id": int(subprocess_id or 0),
        "folio": normalized_folio,
    }

    query = load_sql("select_volume_test_runs.sql")

    engine = get_engine()

    jobs_df = pd.read_sql(
        query,
        engine,
        params=params,
    )

    if jobs_df.empty:
        return jobs_df

    datetime_columns = [
        "business_date",
        "executed_at",
        "started_cdmx",
        "ended_cdmx",
    ]

    for column in datetime_columns:
        if column in jobs_df.columns:
            jobs_df[column] = pd.to_datetime(
                jobs_df[column],
                errors="coerce",
            )

    jobs_df["started_cdmx"] = pd.to_datetime(jobs_df["started_cdmx"], errors="coerce")
    jobs_df["ended_cdmx"] = pd.to_datetime(jobs_df["ended_cdmx"], errors="coerce")
    jobs_df["executed_at"] = pd.to_datetime(jobs_df["executed_at"], errors="coerce").dt.date
    
    return jobs_df
