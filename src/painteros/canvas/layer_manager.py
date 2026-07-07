from __future__ import annotations

from typing import Dict, Iterable

from painteros.canvas.layer import CanvasLayer


class LayerManager:
    """
    Registry dei layer disponibili nel Canvas.

    Non contiene i dati dei pixel.
    Contiene solo la descrizione dei layer.

    I dati sono memorizzati nelle Tile.
    """

    def __init__(self):

        self._layers: Dict[str, CanvasLayer] = {}

    def add(self, layer: CanvasLayer) -> None:

        if layer.name in self._layers:
            raise ValueError(f"Layer '{layer.name}' already exists.")

        self._layers[layer.name] = layer

    def remove(self, name: str) -> None:

        self._layers.pop(name, None)

    def get(self, name: str) -> CanvasLayer:

        return self._layers[name]

    def exists(self, name: str) -> bool:

        return name in self._layers

    def clear(self):

        self._layers.clear()

    def names(self):

        return tuple(sorted(self._layers.keys()))

    def all(self) -> Iterable[CanvasLayer]:

        return self._layers.values()

    def __getitem__(self, name: str):

        return self.get(name)

    def __contains__(self, name: str):

        return self.exists(name)

    def __len__(self):

        return len(self._layers)