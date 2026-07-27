from datetime import datetime, timedelta

from dash import html
import dash_mantine_components as dmc

from src.dbx_monitor.components.test_scenarios import (
    get_test_scenario_options,
)
from src.dbx_monitor.repositories.test_scenario_repository import (
    get_test_scenarios,
)
from src.dbx_monitor.repositories.subprocess_repository import get_subprocesses
from src.dbx_monitor.components.subprocesses import get_subprocess_options


def get_default_date_range() -> tuple[str, str]:
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = today - timedelta(days=1)
    end_date = today - timedelta(milliseconds=1)

    return start_date.isoformat(), end_date.isoformat()


def create_volume_test_filters():
    start_date, end_date = get_default_date_range()
    scenarios_df = get_test_scenarios()

    scenario_options = get_test_scenario_options(
        scenarios_df,
    )

    subprocess_list = get_subprocesses()
    subprocess_options = get_subprocess_options(subprocess_list)

    return html.Div(
        [
            html.Div(
                [
                    dmc.Text("From:", fw=500, w=70),
                    dmc.DateTimePicker(
                        id="volume_start_date",
                        value=start_date,
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
                        id="volume_end_date",
                        value=end_date,
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
                    dmc.Text(
                        "Escenario:",
                        fw=500,
                        w=80,
                    ),
                    dmc.Select(
                        id="volume_scenario",
                        data=scenario_options,
                        value="0",
                        searchable=True,
                        clearable=False,
                        w=260,
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
                        id="volume_subprocess",
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
                    dmc.Text(
                        "Folio:",
                        fw=500,
                        w=55,
                    ),
                    dmc.TextInput(
                        id="volume_folio",
                        placeholder="Número de folio",
                        w=230,
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "gap": "10px",
                },
            ),
            dmc.Button(
                "Buscar",
                id="volume_search_button",
                n_clicks=0,
                variant="filled",
            ),
        ],
        style={
            "display": "flex",
            "gap": "25px",
            "alignItems": "center",
            "flexWrap": "wrap",
            "marginBottom": "15px",
        },
    )
