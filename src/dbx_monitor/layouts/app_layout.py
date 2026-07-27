import dash
from dash import dcc, html
import dash_mantine_components as dmc


def create_navigation():
    return dmc.Paper(
        [
            dmc.Group(
                [
                    dmc.Title(
                        "Databricks Monitor",
                        order=3,
                    ),
                    dmc.Group(
                        [
                            dcc.Link(
                                dmc.Button(
                                    "Inicio",
                                    variant="subtle",
                                ),
                                href="/",
                                style={"textDecoration": "none"},
                            ),
                            dcc.Link(
                                dmc.Button(
                                    "Monitor de ejecuciones",
                                    variant="subtle",
                                ),
                                href="/monitor",
                                style={"textDecoration": "none"},
                            ),
                            dcc.Link(
                                dmc.Button(
                                    "Pruebas de volumen",
                                    variant="subtle",
                                ),
                                href="/volume-tests",
                                style={"textDecoration": "none"},
                            ),
                        ],
                        gap="sm",
                    ),
                ],
                justify="space-between",
                align="center",
            )
        ],
        shadow="sm",
        radius=0,
        p="md",
        withBorder=True,
    )


def create_app_layout():
    return html.Div(
        [
            dcc.Location(id="url"),
            create_navigation(),
            html.Main(
                dash.page_container,
                style={
                    "padding": "20px",
                    "minHeight": "calc(100vh - 80px)",
                    "backgroundColor": "#f8f9fa",
                },
            ),
        ]
    )