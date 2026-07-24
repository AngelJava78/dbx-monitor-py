from dash import Input, Output, State

from src.dbx_monitor.components.badges import create_statistics_badges
from src.dbx_monitor.components.charts import (
    create_cluster_chart,
    create_empty_chart,
)
from src.dbx_monitor.repositories.cluster_repository import (
    get_cluster_usage_by_range_of_date,
)
from src.dbx_monitor.repositories.jobs_repository import get_jobs_by_range_of_date
from src.dbx_monitor.services.cluster_service import (
    prepare_cluster_stack,
)
from src.dbx_monitor.services.jobs_service import (
    filter_jobs_by_folio_number,
    format_jobs_for_grid,
    filter_jobs_by_job_name,
    filter_jobs_by_subprocess_id,
    filter_jobs_by_substage_id,
)


def register_search_callbacks(app):
    @app.callback(
        Output("cluster_chart", "figure"),
        Output("jobs_table", "rowData"),
        Output("metrics_bar", "children"),
        Input("search_button", "n_clicks"),
        State("start_date", "value"),
        State("end_date", "value"),
        State("subprocess_txt", "value"),
        State("substage_txt", "value"),
        State("folio_txt", "value"),
        State("job_name_txt", "value"),
    )
    def search(
        n_clicks, start_date, end_date, subprocess, substage, folio_number, job_name
    ):
        print("*** Folio search ***")

        if not start_date or not end_date:
            return create_empty_chart(), [], []

        print(f"Start date: {start_date}")
        print(f"End date: {end_date}")
        jobs_df = get_jobs_by_range_of_date(start_date, end_date)

        if subprocess not in (None, ""):
            subprocess_id = int(subprocess)
            print(f"Subprocess: {subprocess_id}")
            filtered_jobs = filter_jobs_by_subprocess_id(jobs_df, subprocess_id)

        if substage not in (None, ""):
            substage_id = int(substage)
            print(f"Substage: {substage_id}")
            filtered_jobs = filter_jobs_by_substage_id(filtered_jobs, substage_id)

        print(f"Folio number: {folio_number}")
        filtered_jobs = filter_jobs_by_folio_number(filtered_jobs, folio_number)

        print(f"Job name: {job_name}")
        filtered_jobs = filter_jobs_by_job_name(filtered_jobs, job_name)

        cluster_df = get_cluster_usage_by_range_of_date(start_date, end_date)

        cluster_stack = prepare_cluster_stack(cluster_df)
        fig_cluster = create_cluster_chart(cluster_stack)

        jobs_grid = format_jobs_for_grid(filtered_jobs)
        toolbar = create_statistics_badges(filtered_jobs, cluster_df)

        return fig_cluster, jobs_grid.to_dict("records"), toolbar
