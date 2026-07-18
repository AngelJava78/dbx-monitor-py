from datetime import datetime, timedelta

from dash import html
import dash_mantine_components as dmc
from src.dbx_monitor.repositories.subprocess_repository import get_subprocesses
from src.dbx_monitor.components.subprocesses import get_subprocess_options
from src.dbx_monitor.repositories.substage_repository import get_substages
from src.dbx_monitor.components.substages import get_substage_options

def get_default_date_range() -> tuple[str, str]:
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha_min = today - timedelta(days=1)
    fecha_max = today - timedelta(milliseconds=1)

    return fecha_min.isoformat(), fecha_max.isoformat()


def create_filters():
    fecha_min, fecha_max = get_default_date_range()
    subprocess_list = get_subprocesses()
    subprocess_options = get_subprocess_options(subprocess_list)
    substage_list = get_substages()
    substage_options = get_substage_options(substage_list)


    return html.Div(
        [
            html.Div(
                [
                    dmc.Text("From:", fw=500, w=60),
                    dmc.DateTimePicker(
                        id="start_date",
                        value=fecha_min,
                        w=150,
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
                    dmc.Text("To:", fw=500, w=60),
                    dmc.DateTimePicker(
                        id="end_date",
                        value=fecha_max,
                        w=150,
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "gap": "10px",
                },
            ),
            # html.Div(
            #     [
            #         dmc.Text("Result"),
            #         dmc.Select(
            #             id="state_filter",
            #             data=state_options,
            #             value="ALL",
            #             w=180,
            #             clearable=False,
            #         ),
            #     ],
            #     style={
            #         "display": "flex",
            #         "alignItems": "center",
            #         "gap": "10px",
            #     },
            # ),
            html.Div(
                [
                    dmc.Text("Subprocess:"),
                    dmc.Select(
                        id="subprocess_filter",
                        data=subprocess_options,
                        value="0",
                        w=180,
                        fw=200,
                        clearable=False,
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
                    dmc.Text("Substage:"),
                    dmc.Select(
                        id="substage_filter",
                        data=substage_options,
                        value="0",
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
            html.Div(
                [
                    dmc.Text("Folio:"),
                    dmc.TextInput(
                        id="folio_filter",
                        placeholder="Folio number",
                        w=180,
                    ),
                    dmc.Button(
                        "Search",
                        id="search_button",
                        n_clicks=0,
                        variant="filled",
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

