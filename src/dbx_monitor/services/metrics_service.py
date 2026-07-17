from datetime import timedelta

import pandas as pd


def calculate_duration_metrics(jobs_df: pd.DataFrame) -> dict:
    if jobs_df.empty or "duration" not in jobs_df.columns:
        return {
            "duration_min": "00:00:00",
            "duration_avg": "00:00:00",
            "duration_max": "00:00:00",
            "duration_sum": "00:00:00",
        }

    durations = jobs_df["duration"].apply(_to_timedelta)
    durations = pd.to_timedelta(durations)

    return {
        "duration_min": str(durations.min()).split(".")[0],
        "duration_avg": str(durations.mean()).split(".")[0],
        "duration_max": str(durations.max()).split(".")[0],
        "duration_sum": str(durations.sum()).split(".")[0],
    }


def get_max_instances(cluster_df: pd.DataFrame) -> int:
    if cluster_df.empty or "total_instances" not in cluster_df.columns:
        return 0

    max_value = cluster_df["total_instances"].max()

    if pd.isna(max_value):
        return 0

    return int(max_value)


def _to_timedelta(value) -> timedelta:
    if pd.isna(value):
        return timedelta(0)

    if isinstance(value, timedelta):
        return value

    if hasattr(value, "hour") and hasattr(value, "minute") and hasattr(value, "second"):
        return timedelta(hours=value.hour, minutes=value.minute, seconds=value.second)

    return pd.to_timedelta(value).to_pytimedelta()
