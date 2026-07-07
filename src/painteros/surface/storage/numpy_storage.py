from __future__ import annotations

import numpy as np

from painteros.surface.storage.storage_backend import StorageBackend


class NumpyStorage(StorageBackend):

    def __init__(

        self,

        width,

        height,

        channels,

        dtype,

        default_value,

    ):

        if channels == 1:

            self._data = np.full(

                (height, width),

                default_value,

                dtype=dtype,

            )

        else:

            self._data = np.full(

                (

                    height,

                    width,

                    channels,

                ),

                default_value,

                dtype=dtype,

            )

    @property
    def shape(self):

        return self._data.shape

    @property
    def dtype(self):

        return self._data.dtype

    @property
    def memory_bytes(self):

        return self._data.nbytes

    def fill(

        self,

        value,

    ):

        self._data.fill(value)

    def get(

        self,

        x,

        y,

    ):

        return self._data[y, x]

    def set(

        self,

        x,

        y,

        value,

    ):

        self._data[y, x] = value

    def raw(self):

        return self._data