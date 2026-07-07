from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from painteros.surface.layer_descriptor import LayerDescriptor
from painteros.surface.storage.numpy_storage import NumpyStorage

@dataclass(slots=True)
class TileLayerStatistics:

    modified_pixels: int = 0

    minimum: float = 0.0

    maximum: float = 0.0

    mean: float = 0.0


class TileLayer:
    """
    Vista di un layer appartenente ad una Tile.

    I dati appartengono sempre alla Tile.
    """

    def __init__(

        self,

        descriptor: LayerDescriptor,

        tile_size: int,

    ):

        self.descriptor = descriptor

        self.statistics = TileLayerStatistics()

        self.dirty = False

        self.dirty_rect = None

        self.last_frame = 0

        self.storage = NumpyStorage(

            tile_size,

            tile_size,

            descriptor.channels,

            descriptor.dtype,

            descriptor.default_value,

        )
        '''
        if descriptor.channels == 1:

            self.data = np.full(

                (tile_size, tile_size),

                descriptor.default_value,

                dtype=descriptor.dtype,

            )

        else:

            self.data = np.full(

                (

                    tile_size,

                    tile_size,

                    descriptor.channels,

                ),

                descriptor.default_value,

                dtype=descriptor.dtype,

            )
            '''

    @property
    def shape(self):

        return self.storage.shape

    @property
    def memory_bytes(self):

        return self.storage.memory_bytes

    def clear(self):

        self.storage.fill(

            self.descriptor.default_value

        )

        self.dirty = False

    def mark_dirty(self, frame: int):

        self.dirty = True

        self.last_frame = frame

    def get(

        self,

        x: int,

        y: int,

    ):

        return self.storage.get(x,y)

    def set(

        self,

        x: int,

        y: int,

        value,

    ):

        self.storage.set(

        x,

        y,

        value,

     )

        self.statistics.modified_pixels += 1

        self.dirty = True