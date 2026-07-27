import dash
from dash import Dash
import dash_mantine_components as dmc

from src.dbx_monitor.callbacks.export_callbacks import register_export_callbacks
from src.dbx_monitor.callbacks.search_callbacks import register_search_callbacks
from src.dbx_monitor.callbacks.tasks_callbacks import register_tasks_callbacks
from src.dbx_monitor.layouts.app_layout import create_app_layout
from src.dbx_monitor.callbacks.volume_test_callbacks import (
    register_volume_test_callbacks,
)

def create_app() -> Dash:
    app = Dash(
        __name__,
        use_pages=True,
        suppress_callback_exceptions=True,
        title="Databricks Monitor",
    )

    app.layout = dmc.MantineProvider(create_app_layout())

    # register_dashboard_callbacks(app)
    register_search_callbacks(app)
    register_volume_test_callbacks(app)    
    register_tasks_callbacks(app)
    register_export_callbacks(app)
    return app


app = create_app()
server = app.server

if __name__ == "__main__":
    app.run(debug=True)
