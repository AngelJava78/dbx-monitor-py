import pandas as pd


def filter_jobs_by_date(
    jobs_df: pd.DataFrame,
    start_date,
    end_date,
) -> pd.DataFrame:
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    return jobs_df[
        (jobs_df["started_cdmx"] >= start_date)
        & (jobs_df["started_cdmx"] <= end_date)
    ].copy()


def format_jobs_for_grid(jobs_df: pd.DataFrame) -> pd.DataFrame:
    formatted_df = jobs_df.copy()

    if "started_cdmx" in formatted_df.columns:
        formatted_df["started_cdmx"] = formatted_df["started_cdmx"].dt.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    if "ended_cdmx" in formatted_df.columns:
        formatted_df["ended_cdmx"] = formatted_df["ended_cdmx"].dt.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    return formatted_df

def filter_jobs_by_state(jobs_df: pd.DataFrame, state_filter: str) -> pd.DataFrame:
    if jobs_df is None or jobs_df.empty:
        return pd.DataFrame()
    
    if not state_filter or state_filter == "ALL":
        return jobs_df.copy()
    
    return jobs_df[jobs_df["result_state"] == state_filter].copy()

def filter_jobs_by_subprocess_id(jobs_df: pd.DataFrame, subprocess_id: int) -> pd.DataFrame:
    if jobs_df is None or jobs_df.empty:
        return pd.DataFrame()
    
    if subprocess_id == 0:
        return jobs_df.copy()
    
    return jobs_df[jobs_df["subprocess_id"] == subprocess_id].copy()

def filter_jobs_by_substage_id(jobs_df: pd.DataFrame, substage_id: int) -> pd.DataFrame:
    if jobs_df is None or jobs_df.empty:
        return pd.DataFrame()
    
    if substage_id == 0:
        return jobs_df.copy()
    
    return jobs_df[jobs_df["substage_id"] == substage_id].copy()

def filter_jobs_by_folio_number(jobs_df: pd.DataFrame, folio_number: str) -> pd.DataFrame:
    if jobs_df is None or jobs_df.empty:
        return pd.DataFrame()
    
    if folio_number is None or not str(folio_number).strip():
        return jobs_df.copy()
    
    return jobs_df[jobs_df["folio_number"] == folio_number].copy()