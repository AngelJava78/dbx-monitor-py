from datetime import datetime, timedelta

import pandas as pd

from src.dbx_monitor.database.connection import get_engine
from src.dbx_monitor.database.queries import load_sql


def get_volume_test_runs(
    scenario_id: int,
    execution_date: str,
    folio: str | None,
) -> pd.DataFrame:
    if not execution_date:
        return pd.DataFrame()

    selected_date = pd.to_datetime(execution_date)

    start_date = selected_date.replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    )

    end_date = start_date + timedelta(days=1)

    normalized_folio = None

    if folio and folio.strip():
        normalized_folio = f"%{folio.strip()}%"

    engine = get_engine()
    query = load_sql("select_volume_test_runs.sql")

    params = {
        "scenario_id": scenario_id,
        "start_date": start_date,
        "end_date": end_date,
        "folio": normalized_folio,
    }

    df = pd.read_sql(
        query,
        engine,
        params=params,
    )

    if df.empty:
        return df

    df["started_cdmx"] = pd.to_datetime(
        df["started_cdmx"],
        errors="coerce",
    )

    df["ended_cdmx"] = pd.to_datetime(
        df["ended_cdmx"],
        errors="coerce",
    )

    return df