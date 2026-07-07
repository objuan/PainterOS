from __future__ import annotations

from dataclasses import dataclass

from painteros.math.rect import Rect


@dataclass(slots=True)
class DirtyRegion:

    tile_row: int

    tile_col: int

    layer: str

    rect: Rect

    frame: int


class DirtyManager:

    def __init__(self):

        self._dirty: list[DirtyRegion] = []

    def add(

        self,

        tile_row: int,

        tile_col: int,

        layer: str,

        rect: Rect,

        frame: int,

    ):

        self._dirty.append(

            DirtyRegion(

                tile_row,

                tile_col,

                layer,

                rect,

                frame,

            )

        )

    def clear(self):

        self._dirty.clear()

    def frame(self, frame):

        return [

            x

            for x in self._dirty

            if x.frame == frame

        ]

    def layer(self, layer):

        return [

            x

            for x in self._dirty

            if x.layer == layer

        ]

    def __len__(self):

        return len(self._dirty)