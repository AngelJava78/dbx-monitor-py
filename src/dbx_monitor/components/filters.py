from datetime import datetime, timedelta

from dash import html
import dash_mantine_components as dmc
from src.dbx_monitor.repositories.state_repository import get_state_list
from src.dbx_monitor.components.states import get_state_options


def get_default_date_range() -> tuple[str, str]:
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha_min = today - timedelta(days=1)
    fecha_max = today - timedelta(milliseconds=1)

    return fecha_min.isoformat(), fecha_max.isoformat()


def create_filters():
    fecha_min, fecha_max = get_default_date_range()
    state_list = get_state_list()
    state_options = get_state_options(state_list)

    return html.Div(
        [
            html.Div(
                [
                    dmc.Text("Fecha/Hora Inicio", fw=500, w=140),
                    dmc.DateTimePicker(
                        id="fecha_inicio",
                        value=fecha_min,
                        w=200,
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "gap": "10px",
                },
            ),
            html.Div(
                [
                    dmc.Text("Fecha/Hora Fin", fw=500, w=140),
                    dmc.DateTimePicker(
                        id="fecha_fin",
                        value=fecha_max,
                        w=200,
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "gap": "10px",
                },
            ),
            html.Div(
                [
                    dmc.Text("Result"),
                    dmc.Select(
                        id="state_filter",
                        data=state_options,
                        value="ALL",
                        w=180,
                        clearable=False,
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "gap": "10px",
                },
            ),
        ],
        style={
            "display": "flex",
            "gap": "30px",
            "alignItems": "center",
        },
    )

