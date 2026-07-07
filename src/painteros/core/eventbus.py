from __future__ import annotations

from collections import defaultdict
from threading import RLock
from typing import Any, Callable


EventHandler = Callable[[Any], None]


class EventBus:

    def __init__(self):

        self._lock = RLock()

        self._handlers = defaultdict(list)

    def subscribe(
        self,
        event_type: type,
        handler: EventHandler,
    ):

        with self._lock:
            self._handlers[event_type].append(handler)

    def unsubscribe(
        self,
        event_type: type,
        handler: EventHandler,
    ):

        with self._lock:

            if handler in self._handlers[event_type]:
                self._handlers[event_type].remove(handler)

    def publish(self, event):

        handlers = []

        with self._lock:
            handlers = list(
                self._handlers[type(event)]
            )

        for h in handlers:
            h(event)

    def clear(self):

        with self._lock:
            self._handlers.clear()

    @property
    def subscriptions(self):

        with self._lock:
            return {
                k.__name__: len(v)
                for k, v in self._handlers.items()
            }