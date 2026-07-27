from dash import Input, Output, State, dcc
from dash.exceptions import PreventUpdate
import pandas as pd

from src.dbx_monitor.repositories.jobs_repository import get_jobs
from src.dbx_monitor.services.jobs_service import filter_jobs_by_date


def register_main_export_callback(app):
    @app.callback(
        Output("download-excel", "data"),
        Input("btn_exportar_excel", "n_clicks"),
        State("start_date", "value"),
        State("end_date", "value"),
        prevent_initial_call=True,
    )
    def export_excel(n_clicks, inicio, fin):
        jobs_df = get_jobs()
        jobs_filtrado = filter_jobs_by_date(jobs_df, inicio, fin)

        if "job_id" in jobs_filtrado.columns:
            jobs_filtrado["job_id"] = jobs_filtrado["job_id"].astype(str)

        if "run_id" in jobs_filtrado.columns:
            jobs_filtrado["run_id"] = jobs_filtrado["run_id"].astype(str)

        return dcc.send_data_frame(
            jobs_filtrado.to_excel,
            "jobs_databricks.xlsx",
            sheet_name="Jobs",
            index=False,
        )


def register_volume_export_callback(app):
    @app.callback(
        Output(
            "volume_download_excel",
            "data",
        ),
        Input(
            "volume_export_button",
            "n_clicks",
        ),
        State(
            "volume_jobs_table",
            "rowData",
        ),
        prevent_initial_call=True,
    )
    def export_volume_jobs(
        n_clicks,
        row_data,
    ):
        if not row_data:
            raise PreventUpdate

        jobs_df = pd.DataFrame(row_data)

        for column in (
            "job_id",
            "run_id",
            "folio_number",
        ):
            if column in jobs_df.columns:
                jobs_df[column] = jobs_df[column].astype("string")

        return dcc.send_data_frame(
            jobs_df.to_excel,
            "volume_test_jobs.xlsx",
            sheet_name="Jobs",
            index=False,
        )

def register_export_callbacks(app):
    register_main_export_callback(app)
    register_volume_export_callback(app)