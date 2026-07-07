from __future__ import annotations

from dataclasses import dataclass

from painteros.math.rect import Rect


@dataclass(slots=True)
class DirtyRegion:

    layer: str

    tile_x: int

    tile_y: int

    rect: Rect

    frame: int


class DirtyManager:

    def __init__(self):

        self._regions: list[DirtyRegion] = []

    def add(

        self,

        layer: str,

        tile_x: int,

        tile_y: int,

        rect: Rect,

        frame: int,

    ):

        self._regions.append(

            DirtyRegion(

                layer,

                tile_x,

                tile_y,

                rect,

                frame,

            )

        )

    def clear(self):

        self._regions.clear()

    def regions(self):

        return tuple(self._regions)

    def frame_regions(

        self,

        frame: int,

    ):

        return [

            r

            for r in self._regions

            if r.frame == frame

        ]

    def layer_regions(

        self,

        layer: str,

    ):

        return [

            r

            for r in self._regions

            if r.layer == layer

        ]

    def __len__(self):

        return len(self._regions)