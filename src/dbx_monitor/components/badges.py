import pandas as pd
import dash_mantine_components as dmc

from src.dbx_monitor.services.metrics_service import (
    calculate_duration_metrics,
    get_max_instances,
)


def create_statistics_badges(jobs_df: pd.DataFrame, cluster_df: pd.DataFrame):
    metrics = calculate_duration_metrics(jobs_df)
    max_instances = get_max_instances(cluster_df)

    return [
        dmc.Badge(f"Max Instances: {max_instances}", color="indigo", size="lg"),
        dmc.Badge(f"Jobs: {len(jobs_df):,}", color="blue", size="lg"),
        dmc.Badge(f"Success: {metrics['success_jobs']}", color="green", size="lg"),
        dmc.Badge(f"Failed: {metrics['failed_jobs']}", color="red", size="lg"),
        dmc.Badge(f"Min: {metrics['duration_min']}", color="cyan", size="lg"),
        dmc.Badge(f"Avg: {metrics['duration_avg']}", color="teal", size="lg"),
        dmc.Badge(f"Max: {metrics['duration_max']}", color="orange", size="lg"),
        dmc.Badge(f"Sum: {metrics['duration_sum']}", color="violet", size="lg"),
    ]
