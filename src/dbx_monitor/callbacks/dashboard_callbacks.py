from dash import Input, Output

from src.dbx_monitor.components.badges import create_statistics_badges
from src.dbx_monitor.components.charts import create_cluster_chart, create_empty_chart
from src.dbx_monitor.repositories.cluster_repository import get_cluster_usage
from src.dbx_monitor.repositories.jobs_repository import get_jobs
from src.dbx_monitor.services.cluster_service import (
    filter_cluster_by_date,
    prepare_cluster_stack,
)
from src.dbx_monitor.services.jobs_service import filter_jobs_by_date, format_jobs_for_grid, filter_jobs_by_state, filter_jobs_by_subprocess_id, filter_jobs_by_substage_id


def register_dashboard_callbacks(app):
    @app.callback(
        Output("cluster_chart", "figure"),
        Output("jobs_table", "rowData"),
        Output("metrics_bar", "children"),
        Input("start_date", "value"),
        Input("end_date", "value"),
        # Input("state_filter", "value"),
        Input("subprocess_txt", "value"),
        Input("substage_txt", "value")
    )
    def refresh_dashboard(inicio, fin, subprocess, substage):
        print("*** Refresh dashboard ***")
        if not inicio or not fin:
            return create_empty_chart(), [], []

        jobs_df = get_jobs()
        cluster_df = get_cluster_usage()

        jobs_filtrado = filter_jobs_by_date(jobs_df, inicio, fin)
        # print(f"Stage: {state}")
        # jobs_filtrado = filter_jobs_by_state(jobs_filtrado, state)


        subprocess_id = int(subprocess)
        print(f"Subprocess: {subprocess_id}")
        jobs_filtrado = filter_jobs_by_subprocess_id(jobs_filtrado, subprocess_id)

        substage_id = int(substage)
        print(f"Substage: {substage_id}")
        jobs_filtrado = filter_jobs_by_substage_id(jobs_filtrado, substage_id)

        cluster_filtrado = filter_cluster_by_date(cluster_df, inicio, fin)

        cluster_stack = prepare_cluster_stack(cluster_filtrado)
        fig_cluster = create_cluster_chart(cluster_stack)

        jobs_grid = format_jobs_for_grid(jobs_filtrado)
        toolbar = create_statistics_badges(jobs_filtrado, cluster_filtrado)

        return fig_cluster, jobs_grid.to_dict("records"), toolbar
