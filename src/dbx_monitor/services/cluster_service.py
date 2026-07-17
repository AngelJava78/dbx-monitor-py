import pandas as pd


def filter_cluster_by_date(
    cluster_df: pd.DataFrame,
    start_date,
    end_date,
) -> pd.DataFrame:
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    return cluster_df[
        (cluster_df["start_time_cdmx"] >= start_date)
        & (cluster_df["start_time_cdmx"] <= end_date)
    ].copy()


def prepare_cluster_stack(cluster_df: pd.DataFrame) -> pd.DataFrame:
    if cluster_df.empty:
        return pd.DataFrame(columns=["start_time_cdmx", "tipo", "cantidad"])

    return cluster_df.melt(
        id_vars=["start_time_cdmx"],
        value_vars=["drivers", "workers"],
        var_name="tipo",
        value_name="cantidad",
    )
