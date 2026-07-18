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
            # Línea 1 de filtros
            html.Div(
                [
                    html.Div(
                        [
                            dmc.Text("From:", fw=500, w=70),
                            dmc.DateTimePicker(
                                id="start_date",
                                value=fecha_min,
                                w=190,
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
                            dmc.Text("To:", fw=500, w=50),
                            dmc.DateTimePicker(
                                id="end_date",
                                value=fecha_max,
                                w=190,
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
                            dmc.Text("Subprocess:", fw=500),
                            dmc.Select(
                                id="subprocess_txt",
                                data=subprocess_options,
                                value="0",
                                w=230,
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
                            dmc.Text("Substage:", fw=500),
                            dmc.Select(
                                id="substage_txt",
                                data=substage_options,
                                value="0",
                                w=230,
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
                    "flexWrap": "wrap",
                    "marginBottom": "12px",
                },
            ),

            # Línea 2 de filtros
            html.Div(
                [
                    html.Div(
                        [
                            dmc.Text("Folio:", fw=500, w=70),
                            dmc.TextInput(
                                id="folio_txt",
                                placeholder="Folio number",
                                w=230,
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
                            dmc.Text("Job name:", fw=500, w=80),
                            dmc.TextInput(
                                id="job_name_txt",
                                placeholder="Job name",
                                w=260,
                            ),
                        ],
                        style={
                            "display": "flex",
                            "alignItems": "center",
                            "gap": "10px",
                        },
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
                    "gap": "30px",
                    "alignItems": "center",
                    "flexWrap": "wrap",
                    "marginBottom": "12px",
                },
            ),
        ],
        style={
            "display": "flex",
            "flexDirection": "column",
            "gap": "4px",
            "marginBottom": "10px",
        },
    )
