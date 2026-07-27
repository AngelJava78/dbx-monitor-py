from datetime import timedelta

import pandas as pd
from dash import Input, Output, State

from src.dbx_monitor.components.badges import (
    create_statistics_badges,
)
from src.dbx_monitor.components.charts import (
    create_cluster_chart,
    create_empty_chart,
)
from src.dbx_monitor.repositories.cluster_repository import (
    get_cluster_usage_by_range_of_date,
)
from src.dbx_monitor.repositories.volume_test_repository import (
    get_volume_test_runs,
)
from src.dbx_monitor.services.cluster_service import (
    prepare_cluster_stack,
)
from src.dbx_monitor.services.jobs_service import (
    format_jobs_for_grid,
)



def register_volume_test_callbacks(app):
    @app.callback(
        Output(
            "volume_cluster_chart",
            "figure",
        ),
        Output(
            "volume_jobs_table",
            "rowData",
        ),
        Output(
            "volume_metrics_bar",
            "children",
        ),
        Input(
            "volume_search_button",
            "n_clicks",
        ),
        State(
            "volume_scenario",
            "value",
        ),
        State(
            "volume_execution_date",
            "value",
        ),
        State(
            "volume_folio",
            "value",
        ),
        prevent_initial_call=True,
    )
    def search_volume_tests(
        n_clicks,
        scenario_value,
        execution_date,
        folio,
    ):
        if not execution_date:
            return (
                create_empty_chart(),
                [],
                [],
            )

        scenario_id = int(
            scenario_value or 0
        )

        selected_date = pd.to_datetime(
            execution_date
        )

        start_date = selected_date.replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        )

        end_date = start_date + timedelta(days=1)

        jobs_df = get_volume_test_runs(
            scenario_id=scenario_id,
            execution_date=execution_date,
            folio=folio,
        )

        cluster_df = (
            get_cluster_usage_by_range_of_date(
                start_date,
                end_date,
            )
        )

        cluster_stack = prepare_cluster_stack(
            cluster_df
        )

        chart = create_cluster_chart(
            cluster_stack
        )

        badges = create_statistics_badges(
            jobs_df,
            cluster_df,
        )

        formatted_jobs = format_jobs_for_grid(
            jobs_df
        )

        return (
            chart,
            formatted_jobs.to_dict("records"),
            badges,
        )