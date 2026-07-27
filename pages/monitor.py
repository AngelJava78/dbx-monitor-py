import dash

from src.dbx_monitor.layouts.main_layout import create_layout


dash.register_page(
    __name__,
    path="/monitor",
    name="Monitor de ejecuciones",
    title="Monitor de ejecuciones",
    order=2,
)


def layout(**kwargs):
    return create_layout()