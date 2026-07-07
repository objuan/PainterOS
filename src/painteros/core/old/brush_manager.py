from __future__ import annotations


class BrushManager:

    def __init__(self):

        self._brushes = {}

    def register(

        self,

        brush,

    ):

        self._brushes[brush.name] = brush

    def get(self, name):

        return self._brushes[name]

    def remove(self, name):

        self._brushes.pop(name, None)

    def clear(self):

        self._brushes.clear()

    def names(self):

        return tuple(self._brushes.keys())