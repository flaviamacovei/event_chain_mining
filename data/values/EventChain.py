import sys
sys.path.append(sys.path[0] + '/..')
from data.values.Event import Event

class EventChain:
    def __init__(self, events: list[Event] = None):
        if events:
            self.events = events
        else:
            self.events = []

    def add_event(self, event: Event):
        self.events.append(event)

    def __str__(self):
        return str(self.events)