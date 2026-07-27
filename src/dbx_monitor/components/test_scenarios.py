import pandas as pd


def get_test_scenario_options(
    scenarios_df: pd.DataFrame,
) -> list[dict[str, str]]:
    options = [
        {
            "value": "0",
            "label": "ALL",
        }
    ]

    if scenarios_df is None or scenarios_df.empty:
        return options

    options.extend(
        {
            "value": str(row.scenario_id),
            "label": row.description,
        }
        for row in scenarios_df.itertuples(index=False)
    )

    return options