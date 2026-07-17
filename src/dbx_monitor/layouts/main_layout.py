from dash import dcc, html
import dash_mantine_components as dmc

from src.dbx_monitor.components.filters import create_filters
from src.dbx_monitor.components.tables import build_column_defs, create_jobs_grid
from src.dbx_monitor.repositories.jobs_repository import get_jobs


def create_layout():
    jobs_df = get_jobs()

    column_defs = build_column_defs(jobs_df.columns)

    return html.Div(
        [
            dmc.Title(
                "Dashboard de Pruebas de volumen de Databricks",
                order=1,
            ),
            create_filters(),
            html.Hr(),
            html.Div(
                dcc.Graph(
                    id="grafica_cluster",
                    config={"displaylogo": False},
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
            dcc.Download(id="download-excel"),
            html.Div(
                [
                    dmc.Button(
                        "Exportar Excel",
                        id="btn_exportar_excel",
                        color="#1f2937",
                    ),
                    html.Div(
                        id="barra_estadisticas",
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
            create_jobs_grid(column_defs),
            html.Br(),
        ],
        style={"padding": "20px"},
    )
