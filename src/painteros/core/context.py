from __future__ import annotations

from painteros.core.services import ServiceContainer


class ApplicationContext:
    """
    Global application context.
    """

    def __init__(self) -> None:

        self.services = ServiceContainer()

    def register(self, name: str, instance) -> None:

        self.services.register_singleton(name, instance)

    def get(self, name: str):

        return self.services.resolve(name)