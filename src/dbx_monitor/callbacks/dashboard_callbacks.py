from dash import Input, Output

from src.dbx_monitor.components.badges import create_statistics_badges
from src.dbx_monitor.components.charts import create_cluster_chart, create_empty_chart
from src.dbx_monitor.repositories.cluster_repository import get_cluster_usage
from src.dbx_monitor.repositories.jobs_repository import get_jobs
from src.dbx_monitor.services.cluster_service import (
    filter_cluster_by_date,
    prepare_cluster_stack,
)
from src.dbx_monitor.services.jobs_service import filter_jobs_by_date, format_jobs_for_grid


def register_dashboard_callbacks(app):
    @app.callback(
        Output("grafica_cluster", "figure"),
        Output("tabla_jobs", "rowData"),
        Output("barra_estadisticas", "children"),
        Input("fecha_inicio", "value"),
        Input("fecha_fin", "value"),
    )
    def actualizar_dashboard(inicio, fin):
        if not inicio or not fin:
            return create_empty_chart(), [], []

        jobs_df = get_jobs()
        cluster_df = get_cluster_usage()

        jobs_filtrado = filter_jobs_by_date(jobs_df, inicio, fin)
        cluster_filtrado = filter_cluster_by_date(cluster_df, inicio, fin)

        cluster_stack = prepare_cluster_stack(cluster_filtrado)
        fig_cluster = create_cluster_chart(cluster_stack)

        jobs_grid = format_jobs_for_grid(jobs_filtrado)
        toolbar = create_statistics_badges(jobs_filtrado, cluster_filtrado)

        return fig_cluster, jobs_grid.to_dict("records"), toolbar
