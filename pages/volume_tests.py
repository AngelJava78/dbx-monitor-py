import dash

from src.dbx_monitor.layouts.volume_test_layout import (
    create_volume_test_layout,
)


dash.register_page(
    __name__,
    path="/volume-tests",
    name="Pruebas de volumen",
    title="Pruebas de volumen",
    order=3,
)


def layout(**kwargs):
    return create_volume_test_layout()