from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(slots=True)
class Event:
    """
    Base class for every PainterOS event.
    """

    event_id: UUID
    simulation_time: float


@dataclass(slots=True)
class StrokeStarted(Event):
    stroke_id: UUID


@dataclass(slots=True)
class StrokeFinished(Event):
    stroke_id: UUID


def new_event(event_type, simulation_time: float, **kwargs):
    """
    Utility to create typed events.
    """
    return event_type(
        event_id=uuid4(),
        simulation_time=simulation_time,
        **kwargs
    )