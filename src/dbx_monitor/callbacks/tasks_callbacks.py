import logging

from dash import Input, Output, State
from dash.exceptions import PreventUpdate

from src.dbx_monitor.components.tasks_grid import (
    build_tasks_column_defs,
    format_tasks_for_grid,
)
from src.dbx_monitor.repositories.tasks_repository import (
    get_tasks_by_run_id,
)

logger = logging.getLogger(__name__)


def register_tasks_callbacks(app):
    logger.warning("Registering tasks callbacks")

    @app.callback(
        Output("tasks_table", "rowData"),
        Output("tasks_table", "columnDefs"),
        Output("tasks_title", "children"),
        Input("jobs_table", "cellClicked"),
        State("jobs_table", "rowData"),
        prevent_initial_call=True,
    )
    def load_tasks(cell_clicked, jobs_row_data):
        logger.warning(
            "jobs_table cellClicked event received: %s",
            cell_clicked,
        )

        if cell_clicked is None:
            logger.warning("cellClicked event is None")
            raise PreventUpdate

        column_id = cell_clicked.get("colId")
        cell_value = cell_clicked.get("value")
        row_index = cell_clicked.get("rowIndex")

        row_data = cell_clicked.get("data") or {}

        job_name = row_data.get("job_name", "Unknown")     

        logger.warning(
            "Clicked column=%s, value=%s",
            column_id,
            cell_value,
        )

        if column_id != "run_id":
            logger.warning(
                "Click ignored because column '%s' is not run_id",
                column_id,
            )
            raise PreventUpdate

        if cell_value is None:
            logger.error("The clicked run_id cell does not contain a value")
            return (
                [],
                [],
                "The selected cell does not contain a run_id",
            )

        try:
            run_id = int(cell_value)
        except (TypeError, ValueError):
            logger.exception(
                "Invalid run_id received: %s",
                cell_value,
            )
            return (
                [],
                [],
                f"Invalid run_id: {cell_value}",
            )

        job_name = "Unknown"

        if (
            jobs_row_data
            and row_index is not None
            and 0 <= row_index < len(jobs_row_data)
        ):
            selected_row = jobs_row_data[row_index]
            job_name = selected_row.get("job_name") or "Unknown"

        logger.warning(
            "Calling tasks repository for run_id=%s",
            run_id,
        )

        try:
            tasks_df = get_tasks_by_run_id(run_id)
        except Exception:
            logger.exception(
                "Failed to load tasks for run_id=%s",
                run_id,
            )
            return (
                [],
                [],
                f"Failed to load tasks for run_id {run_id}",
            )

        logger.warning(
            "Repository returned %s task records for run_id=%s",
            len(tasks_df),
            run_id,
        )

        if tasks_df.empty:
            return (
                [],
                [],
                f"No tasks were found for run_id {run_id}",
            )

        tasks_df = format_tasks_for_grid(tasks_df)
        tasks_column_defs = build_tasks_column_defs(tasks_df.columns)

        return (
            tasks_df.to_dict("records"),
            tasks_column_defs,
            f"Tasks for job name: {job_name} | run_id: {run_id}",
        )
