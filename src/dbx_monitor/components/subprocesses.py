from src.dbx_monitor.models.subprocess import Subprocess
def get_subprocess_options(subprocesses: list[Subprocess]) -> list[dict]:
    default_option = [
        {
            "label": "ALL",
            "value": "0"
        }
    ]
    options = [
        {
            "label": s.subprocess_name,
            "value": str(s.subprocess_id)
        }
        for s in subprocesses
    ]
    return default_option + options