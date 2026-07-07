from .clock import SimulationClock
from .eventbus import EventBus


class PainterApplication:
    def __init__(self):
        self.events = EventBus()
        self.clock = SimulationClock()
