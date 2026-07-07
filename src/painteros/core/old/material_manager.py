from __future__ import annotations

from typing import Dict

from painteros.surface.material import Material


class MaterialManager:

    """
    Libreria dei materiali disponibili.
    """

    def __init__(self):

        self._materials: Dict[str, Material] = {}

    def register(

        self,

        name: str,

        material: Material,

    ):

        self._materials[material.uuid] = material

    def get(self, uuid):

        return self._materials[uuid]


    def exists(self, uuid):

        return uuid in self._materials

    def remove(self, uuid):

        self._materials.pop(uuid, None)

    def clear(self):

        self._materials.clear()

    def __len__(self):

        return len(self._materials)