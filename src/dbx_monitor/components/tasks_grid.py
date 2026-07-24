import dash_ag_grid as dag
import pandas as pd

def build_tasks_column_defs(columns) -> list[dict]:
    column_defs = []

    for column in columns:
        if column == "run_page_url":
            continue        
        col_def = {
            "field": column,
            "sortable": True,
            "resizable": True,
        }

        if column == "task_run_id":
            col_def.update(
                {
                    "headerName": "task_run_id",
                    "minWidth": 160,
                    "cellRenderer": "TaskRunLink",
                }
            )

        if column in ["task_key", "task_name", "notebook_path"]:
            col_def["minWidth"] = 250

        elif column in ["run_id", "job_id"]:
            col_def["minWidth"] = 140

        column_defs.append(col_def)

    return column_defs



def create_tasks_grid():
    return dag.AgGrid(
        id="tasks_table",
        rowData=[],
        columnDefs=[],
        defaultColDef={
            "sortable": True,
            "resizable": True,
            "minWidth": 120,
        },
        columnSize="autoSize",
        className="ag-theme-alpine",
        style={
            "height": "400px",
            "width": "100%",
            "fontSize": "10px",
            "borderRadius": "10px",
            "overflow": "hidden",
            "boxShadow": "0 2px 8px rgba(0,0,0,0.1)",
        },
        dashGridOptions={
            "pagination": True,
            "paginationPageSize": 20,
            "animateRows": True,
            "rowHeight": 28,
            "headerHeight": 32,
        },
    )

def format_tasks_for_grid(tasks_df: pd.DataFrame) -> pd.DataFrame:
    formatted_df = tasks_df.copy()

    datetime_columns = [
        "started_cdmx",
        "ended_cdmx",
    ]

    for column in datetime_columns:
        if column in formatted_df.columns:
            formatted_df[column] = pd.to_datetime(
                formatted_df[column],
                errors="coerce",
            ).dt.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_df