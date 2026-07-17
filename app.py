from dash import Dash
import dash_mantine_components as dmc

from src.dbx_monitor.callbacks.dashboard_callbacks import register_dashboard_callbacks
from src.dbx_monitor.callbacks.export_callbacks import register_export_callbacks
from src.dbx_monitor.layouts.main_layout import create_layout


def create_app() -> Dash:
    app = Dash(__name__)

    app.layout = dmc.MantineProvider(
        create_layout()
    )

    register_dashboard_callbacks(app)
    register_export_callbacks(app)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
