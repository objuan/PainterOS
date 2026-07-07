from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class StorageBackend(ABC):

    """
    Backend astratto per la memorizzazione
    dei dati di un TileLayer.
    """

    @property
    @abstractmethod
    def shape(self):
        ...

    @property
    @abstractmethod
    def dtype(self):
        ...

    @property
    @abstractmethod
    def memory_bytes(self):
        ...

    @abstractmethod
    def fill(self, value):
        ...

    @abstractmethod
    def get(self, x, y):
        ...

    @abstractmethod
    def set(self, x, y, value):
        ...

    @abstractmethod
    def raw(self):
        ...