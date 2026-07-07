from __future__ import annotations

from painteros.surface.statistics import SurfaceStatistics
from painteros.surface.layer_manager import LayerManager
from painteros.surface.tile_manager import TileManager
from painteros.surface.dirty_manager import DirtyManager


class SurfaceState:

    def __init__(

        self,

        width: int,

        height: int,

        tile_size: int = 256,

    ):

        self.statistics = SurfaceStatistics()

        self.layers = LayerManager()

        self.dirty = DirtyManager()

        self.tiles = TileManager(

            width,

            height,

            self.layers,

            tile_size,

        )

    def begin_frame(self):

        self.statistics.next_frame()

        self.dirty.clear()

    def end_frame(self):

        pass