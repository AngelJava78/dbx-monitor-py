import dash
from dash import dcc, html
import dash_mantine_components as dmc


dash.register_page(
    __name__,
    path="/",
    name="Inicio",
    title="Databricks Monitor",
    order=1,
)


def create_dashboard_card(
    title: str,
    description: str,
    path: str,
    button_text: str,
):
    return dmc.Card(
        [
            dmc.Stack(
                [
                    dmc.Title(
                        title,
                        order=3,
                    ),
                    dmc.Text(
                        description,
                        c="dimmed",
                    ),
                    dcc.Link(
                        dmc.Button(
                            button_text,
                            fullWidth=True,
                        ),
                        href=path,
                        style={"textDecoration": "none"},
                    ),
                ],
                gap="md",
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        padding="lg",
        style={
            "width": "360px",
            "minHeight": "230px",
        },
    )


layout = html.Div(
    [
        dmc.Stack(
            [
                dmc.Title(
                    "Panel de monitoreo de Databricks",
                    order=1,
                ),
                dmc.Text(
                    (
                        "Selecciona uno de los dashboards disponibles "
                        "para consultar ejecuciones y pruebas."
                    ),
                    size="lg",
                    c="dimmed",
                ),
                dmc.SimpleGrid(
                    [
                        create_dashboard_card(
                            title="Monitor de ejecuciones",
                            description=(
                                "Consulta jobs, runs, tareas, consumo "
                                "del clúster y métricas de ejecución."
                            ),
                            path="/monitor",
                            button_text="Abrir dashboard",
                        ),
                        create_dashboard_card(
                            title="Pruebas de volumen",
                            description=(
                                "Administra escenarios basados en "
                                "ejecuciones productivas y compara "
                                "sus resultados en QA."
                            ),
                            path="/volume-tests",
                            button_text="Abrir dashboard",
                        ),
                    ],
                    cols={
                        "base": 1,
                        "md": 2,
                    },
                    spacing="lg",
                ),
            ],
            gap="xl",
        )
    ]
)