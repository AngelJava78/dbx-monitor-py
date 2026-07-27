from datetime import datetime

from dash import html
import dash_mantine_components as dmc

from src.dbx_monitor.components.test_scenarios import (
    get_test_scenario_options,
)
from src.dbx_monitor.repositories.test_scenario_repository import (
    get_test_scenarios,
)


def create_volume_test_filters():
    scenarios_df = get_test_scenarios()

    scenario_options = get_test_scenario_options(
        scenarios_df,
    )

    today = datetime.now().replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
    )

    return html.Div(
        [
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
                    dmc.Text(
                        "Fecha:",
                        fw=500,
                        w=60,
                    ),
                    dmc.DateTimePicker(
                        id="volume_execution_date",
                        value=today.isoformat(),
                        w=210,
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