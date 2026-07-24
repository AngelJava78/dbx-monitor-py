import dash_ag_grid as dag


def build_column_defs(columns) -> list[dict]:
    column_defs = []

    for col in columns:
        if col == "run_page_url":
            continue

        col_def = {
            "field": col,
            "sortable": True,
            "resizable": True,
        }

        if col == "job_name":
            col_def["minWidth"] = 350
            col_def["cellStyle"] = {
                "userSelect": "text",
                "cursor": "text",
            }

        elif col == "duration":
            col_def["minWidth"] = 100
            col_def["cellRenderer"] = "RunDurationLink"

        elif col == "job_id":
            col_def["minWidth"] = 140
            col_def["cellRenderer"] = "DatabricksJobLink"

        elif col == "run_id":
            col_def["minWidth"] = 140
            col_def["cellStyle"] = {
                "color": "#0563C1",
                "textDecoration": "underline",
                "cursor": "pointer",
                "userSelect": "text",
            }
        elif col == "folio_number":
            col_def["cellStyle"] = {
                "userSelect": "text",
                "cursor": "text",
            }


        column_defs.append(col_def)

    return column_defs


def create_jobs_grid(column_defs: list[dict]):
    return dag.AgGrid(
        id="jobs_table",
        rowData=[],
        columnDefs=column_defs,
        defaultColDef={
            "sortable": True,
            "resizable": True,
            "minWidth": 100,
        },
        columnSize="autoSize",
        className="ag-theme-alpine",
        style={
            "height": "700px",
            "width": "100%",
            "fontSize": "9px",
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
