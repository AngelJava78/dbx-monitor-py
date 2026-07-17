from datetime import datetime, timedelta

from dash import html
import dash_mantine_components as dmc


def get_default_date_range() -> tuple[str, str]:
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha_min = today - timedelta(days=1)
    fecha_max = today - timedelta(milliseconds=1)

    return fecha_min.isoformat(), fecha_max.isoformat()


def create_date_filters():
    fecha_min, fecha_max = get_default_date_range()

    return html.Div(
        [
            html.Div(
                [
                    dmc.Text("Fecha/Hora Inicio", fw=500, w=140),
                    dmc.DateTimePicker(
                        id="fecha_inicio",
                        value=fecha_min,
                        w=250,
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
                        w=250,
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
