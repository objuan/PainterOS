from uuid import uuid4

from painteros.core.eventbus import EventBus
from painteros.core.events import StrokeStarted


def test_publish():

    bus = EventBus()

    received = []

    def handler(event):
        received.append(event)

    bus.subscribe(StrokeStarted, handler)

    bus.publish(
        StrokeStarted(
            event_id=uuid4(),
            simulation_time=0.0,
            stroke_id=uuid4(),
        )
    )

    assert len(received) == 1


def test_unsubscribe():

    bus = EventBus()

    called = []

    def handler(event):
        called.append(1)

    bus.subscribe(StrokeStarted, handler)
    bus.unsubscribe(StrokeStarted, handler)

    bus.publish(
        StrokeStarted(
            event_id=uuid4(),
            simulation_time=0,
            stroke_id=uuid4(),
        )
    )

    assert len(called) == 0