from __future__ import annotations

from typing import Dict

from painteros.surface.storage.storage_backend import StorageBackend


class StorageManager:

    """
    Registry di tutti gli storage del motore.
    """

    def __init__(self):

        self._storages: Dict[str, StorageBackend] = {}

    def register(

        self,

        name: str,

        storage: StorageBackend,

    ):

        if name in self._storages:
            raise ValueError(name)

        self._storages[name] = storage

    def get(self, name):

        return self._storages[name]

    def remove(self, name):

        self._storages.pop(name, None)

    def clear(self):

        self._storages.clear()

    def names(self):

        return tuple(self._storages.keys())

    def __len__(self):

        return len(self._storages)