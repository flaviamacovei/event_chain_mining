import sys
sys.path.append(sys.path[0] + '/..')
from data.values.Event import Event

def load(transformed_data: list):
    assert transformed_data and len(transformed_data) > 0, "transformed_data is empty"
    events = []
    for event_info in transformed_data:
        action = event_info.pop(0)
        if event_info:
            event_dict = {item[0]: item[1] for item in event_info}
            events.append(Event(action = action, **event_dict))
    return events