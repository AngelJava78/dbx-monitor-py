import logging

import dash_mantine_components as dmc
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

logger = logging.getLogger(__name__)


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
            "volume_start_date",
            "value",
        ),
        State(
            "volume_end_date",
            "value",
        ),
        State(
            "volume_scenario",
            "value",
        ),
        State(
            "volume_subprocess",
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
        start_date,
        end_date,
        scenario_value,
        subprocess_value,
        folio,
    ):
        if not start_date or not end_date:
            return (
                create_empty_chart(),
                [],
                [
                    dmc.Alert(
                        "Start date and end date are required.",
                        color="red",
                    )
                ],
            )

        try:
            scenario_id = int(scenario_value or 0)

            subprocess_id = int(subprocess_value or 0)

            parsed_start_date = pd.to_datetime(
                start_date,
                errors="raise",
            )

            parsed_end_date = pd.to_datetime(
                end_date,
                errors="raise",
            )

            if parsed_start_date >= parsed_end_date:
                return (
                    create_empty_chart(),
                    [],
                    [
                        dmc.Alert(
                            ("The start date must be earlier " "than the end date."),
                            color="red",
                        )
                    ],
                )

            jobs_df = get_volume_test_runs(
                start_date=start_date,
                end_date=end_date,
                scenario_id=scenario_id,
                subprocess_id=subprocess_id,
                folio=folio,
            )

            if jobs_df.empty:
                return (
                    create_empty_chart(),
                    [],
                    [
                        dmc.Alert(
                            ("No executions were found for " "the selected filters."),
                            color="yellow",
                        )
                    ],
                )

            cluster_df = get_cluster_usage_by_range_of_date(
                parsed_start_date.to_pydatetime(),
                parsed_end_date.to_pydatetime(),
            )

            cluster_stack = prepare_cluster_stack(cluster_df)

            chart = create_cluster_chart(cluster_stack)

            metrics = create_statistics_badges(
                jobs_df,
                cluster_df,
            )

            formatted_jobs_df = format_jobs_for_grid(jobs_df)

            return (
                chart,
                formatted_jobs_df.to_dict("records"),
                metrics,
            )

        except (TypeError, ValueError) as exc:
            logger.warning(
                "Invalid volume-test filters: %s",
                exc,
            )

            return (
                create_empty_chart(),
                [],
                [
                    dmc.Alert(
                        str(exc),
                        color="red",
                    )
                ],
            )

        except Exception:
            logger.exception("Failed to load volume-test data.")

            return (
                create_empty_chart(),
                [],
                [
                    dmc.Alert(
                        ("An error occurred while loading " "the volume-test data."),
                        color="red",
                    )
                ],
            )
