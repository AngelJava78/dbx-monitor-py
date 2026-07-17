
def get_state_options(states: list[str]) -> list[dict]:
    return [{"label": "ALL", "value": "ALL"}] + [
        {"label": state, "value": state}
        for state in states
    ]
        
    