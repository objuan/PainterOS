from __future__ import annotations

from typing import Any, Callable

Factory = Callable[[], Any]


class ServiceContainer:
    """
    Simple Dependency Injection container.
    """

    def __init__(self) -> None:
        self._singletons: dict[str, Any] = {}
        self._factories: dict[str, Factory] = {}

    def register_singleton(self, name: str, instance: Any) -> None:
        if self.has(name):
            raise ValueError(f"Service '{name}' already registered.")
        self._singletons[name] = instance

    def register_factory(self, name: str, factory: Factory) -> None:
        if self.has(name):
            raise ValueError(f"Service '{name}' already registered.")
        self._factories[name] = factory

    def resolve(self, name: str) -> Any:
        if name in self._singletons:
            return self._singletons[name]

        if name in self._factories:
            return self._factories[name]()

        raise KeyError(f"Service '{name}' not found.")

    def has(self, name: str) -> bool:
        return (
            name in self._singletons
            or name in self._factories
        )

    def remove(self, name: str) -> None:
        self._singletons.pop(name, None)
        self._factories.pop(name, None)

    def clear(self) -> None:
        self._singletons.clear()
        self._factories.clear()

    @property
    def services(self) -> tuple[str, ...]:
        return tuple(sorted(
            list(self._singletons.keys()) +
            list(self._factories.keys())
        ))