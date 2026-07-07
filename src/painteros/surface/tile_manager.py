from __future__ import annotations

from painteros.canvas.tile import Tile
from painteros.canvas.tile import TileGeometry
from painteros.canvas.tile import TileIndex

from painteros.math.rect import Rect
from painteros.surface.tile_layer import TileLayer


class TileManager:

    def __init__(

        self,

        width,

        height,

        layer_manager,

        tile_size=256,

    ):

        self.width = width

        self.height = height

        self.tile_size = tile_size

        self.layer_manager = layer_manager

        self._tiles = {}

    def create_tile(

        self,

        row,

        col,

    ):

        key = (row, col)

        if key in self._tiles:

            return self._tiles[key]

        geometry = TileGeometry(

            TileIndex(row, col),

            Rect(

                col * self.tile_size,

                row * self.tile_size,

                self.tile_size,

                self.tile_size,

            ),

            self.tile_size,

        )

        tile = Tile(geometry)

        for descriptor in self.layer_manager:

            tile.add_layer(

                TileLayer(

                    descriptor,

                    self.tile_size,

                )

            )

        self._tiles[key] = tile

        return tile

    def get(

        self,

        row,

        col,

    ):

        return self._tiles.get((row, col))

    def tile_at(

        self,

        x,

        y,

    ):

        row = y // self.tile_size

        col = x // self.tile_size

        return self.create_tile(row, col)

    def clear(self):

        self._tiles.clear()

    def __iter__(self):

        return iter(self._tiles.values())

    def __len__(self):

        return len(self._tiles)