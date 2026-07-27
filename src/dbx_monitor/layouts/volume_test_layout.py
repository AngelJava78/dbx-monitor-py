from dash import dcc, html
import dash_mantine_components as dmc

from src.dbx_monitor.components.tables import (
    build_column_defs,
    create_jobs_grid,
)
from src.dbx_monitor.components.tasks_grid import (
    create_tasks_grid,
)
from src.dbx_monitor.components.volume_test_filters import (
    create_volume_test_filters,
)
from src.dbx_monitor.repositories.jobs_repository import (
    get_jobs,
)


def create_volume_test_layout():
    jobs_df = get_jobs()
    column_defs = build_column_defs(jobs_df.columns)

    return html.Div(
        [
            dmc.Title(
                "Pruebas de volumen y estrés",
                order=1,
            ),
            dmc.Text(
                (
                    "Reproducción en QA de escenarios observados "
                    "originalmente en producción."
                ),
                c="dimmed",
                mb="md",
            ),
            create_volume_test_filters(),
            html.Hr(),
            html.Div(
                dcc.Graph(
                    id="volume_cluster_chart",
                    config={
                        "displaylogo": False,
                    },
                ),
                style={
                    "borderRadius": "10px",
                    "overflow": "hidden",
                    "boxShadow": "0 2px 8px rgba(0,0,0,0.1)",
                    "backgroundColor": "white",
                    "padding": "10px",
                },
            ),
            html.Hr(),
            dcc.Download(
                id="volume_download_excel",
            ),
            html.Div(
                [
                    dmc.Button(
                        "Export",
                        id="volume_export_button",
                        color="#1f2937",
                    ),
                    html.Div(
                        id="volume_metrics_bar",
                        style={
                            "display": "flex",
                            "alignItems": "center",
                            "gap": "10px",
                            "flexWrap": "wrap",
                        },
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "gap": "10px",
                    "marginBottom": "10px",
                },
            ),
            create_jobs_grid(
                column_defs,
                grid_id="volume_jobs_table",
            ),
            html.Br(),
            dmc.Title(
                "Seleccione un run_id para consultar sus tareas",
                id="volume_tasks_title",
                order=3,
            ),
            dcc.Loading(
                type="circle",
                children=create_tasks_grid(
                    grid_id="volume_tasks_table",
                ),
            ),
            html.Br(),
        ],
        style={
            "width": "100%",
        },
    )