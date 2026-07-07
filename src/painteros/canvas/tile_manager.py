from __future__ import annotations

import math

from painteros.canvas.tile import Tile
from painteros.canvas.tile import TileGeometry
from painteros.canvas.tile import TileIndex

from painteros.math.rect import Rect


class TileManager:

    """
    Gestione delle Tile.

    Le Tile vengono create Lazy.

    """

    def __init__(

        self,

        width: int,

        height: int,

        tile_size: int = 256,

    ):

        self.width = width

        self.height = height

        self.tile_size = tile_size

        self.rows = math.ceil(height / tile_size)

        self.cols = math.ceil(width / tile_size)

        self._tiles = {}

    def tile_index(

        self,

        x: int,

        y: int,

    ) -> TileIndex:

        return TileIndex(

            y // self.tile_size,

            x // self.tile_size,

        )

    def create_tile(

        self,

        row: int,

        col: int,

    ) -> Tile:

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

        tile = Tile(

            geometry,

        )

        self._tiles[key] = tile

        return tile

    def get_tile(

        self,

        row: int,

        col: int,

    ) -> Tile | None:

        return self._tiles.get((row, col))

    def tile_at(

        self,

        x: int,

        y: int,

    ) -> Tile:

        index = self.tile_index(x, y)

        return self.create_tile(

            index.row,

            index.col,

        )

    def remove_tile(

        self,

        row: int,

        col: int,

    ):

        self._tiles.pop(

            (row, col),

            None,

        )

    def clear(self):

        self._tiles.clear()

    def tiles(self):

        return self._tiles.values()

    def loaded_tiles(self):

        return len(self._tiles)

    def tiles_in_rect(

        self,

        rect: Rect,

    ):

        r0 = rect.top // self.tile_size
        r1 = rect.bottom // self.tile_size

        c0 = rect.left // self.tile_size
        c1 = rect.right // self.tile_size

        result = []

        for r in range(r0, r1 + 1):

            for c in range(c0, c1 + 1):

                result.append(

                    self.create_tile(r, c)

                )

        return result

    def __len__(self):

        return len(self._tiles)