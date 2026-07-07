from __future__ import annotations

from typing import Dict, Iterable

from painteros.surface.layer_descriptor import LayerDescriptor


class LayerManager:

    """
    Registry globale dei layer del Surface.
    """

    def __init__(self):

        self._layers: Dict[str, LayerDescriptor] = {}

    def register(
        self,
        descriptor: LayerDescriptor,
    ):

        if descriptor.name in self._layers:
            raise ValueError(
                f"Layer '{descriptor.name}' already registered."
            )

        self._layers[descriptor.name] = descriptor

    def unregister(
        self,
        name: str,
    ):

        self._layers.pop(name, None)

    def get(
        self,
        name: str,
    ) -> LayerDescriptor:

        return self._layers[name]

    def exists(
        self,
        name: str,
    ):

        return name in self._layers

    def descriptors(self):

        return tuple(self._layers.values())

    def names(self):

        return tuple(self._layers.keys())

    def clear(self):

        self._layers.clear()

    def __iter__(self):

        return iter(self._layers.values())

    def __len__(self):

        return len(self._layers)

    def __getitem__(self, name):

        return self.get(name)