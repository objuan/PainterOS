from __future__ import annotations

from typing import Dict

from painteros.surface.tile_layer import TileLayer
from painteros.surface.cell_grid import CellGrid

class Tile:

    def __init__(

        self,

        geometry,

    ):

        self.geometry = geometry

        self.grid = CellGrid(geometry.size)

        self.layers: Dict[str, TileLayer] = {}
        # self.layers = {}

        self.loaded = True

        self.locked = False

    def add_layer(

        self,

        layer: TileLayer,

    ):

        self.layers[

            layer.descriptor.name

        ] = layer

    def layer(

        self,

        name: str,

    ) -> TileLayer:

        return self.layers[name]

    @property
    def memory_bytes(self):

        return sum(

            x.memory_bytes

            for x in self.layers.values()

        )