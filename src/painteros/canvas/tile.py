from __future__ import annotations

from dataclasses import dataclass, field
import numpy as np

from painteros.canvas.layer import CanvasLayer


@dataclass(slots=True)
class TileIndex:
    row: int
    col: int


@dataclass(slots=True)
class TileGeometry:

    index: TileIndex

    bounds: "Rect"

    size: int = 256

    def canvas_to_local(self, x: int, y: int):

        return (
            x - self.bounds.x,
            y - self.bounds.y,
        )

    def local_to_canvas(self, x: int, y: int):

        return (
            self.bounds.x + x,
            self.bounds.y + y,
        )


class Tile:

    def __init__(

        self,

        geometry: TileGeometry,

    ):

        self.geometry = geometry

        self.layers: dict[str, np.ndarray] = {}

        self.dirty = False

        self.loaded = True

    def has_layer(self, name: str):

        return name in self.layers

    def create_layer(

        self,

        layer: CanvasLayer,

    ):

        if layer.channels == 1:

            data = np.zeros(

                (

                    self.geometry.size,

                    self.geometry.size,

                ),

                dtype=layer.dtype,

            )

        else:

            data = np.zeros(

                (

                    self.geometry.size,

                    self.geometry.size,

                    layer.channels,

                ),

                dtype=layer.dtype,

            )

        self.layers[layer.name] = data

    def get_layer(self, name: str):

        return self.layers[name]

    def remove_layer(self, name: str):

        self.layers.pop(name, None)

    def clear(self):

        self.layers.clear()

    @property
    def memory_bytes(self):

        return sum(

            x.nbytes

            for x in self.layers.values()

        )