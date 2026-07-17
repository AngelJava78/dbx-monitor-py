from src.dbx_monitor.models.substage import Substage
def get_substage_options(substages: list[Substage]) -> list[dict]:
    default_option = [
        {
            "label": "ALL", 
            "value": "0"
        }
    ]
    options = [
        {
            "label": s.substage_name, 
            "value": str(s.substage_id)
        }
        for s in substages
    ]
    return default_option + options