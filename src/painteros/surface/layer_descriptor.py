from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from painteros.surface.layer_type import LayerType


@dataclass(slots=True, frozen=True)
class LayerDescriptor:
    """
    Descrive un layer.

    NON contiene dati.

    Viene condiviso da tutte le Tile.
    """

    name: str

    layer_type: LayerType

    channels: int = 1

    dtype: Any = np.float32

    default_value: float = 0.0

    physical_unit: str = ""

    visible: bool = True

    persistent: bool = True

    interpolated: bool = True

    compressible: bool = True

    description: str = ""

    def is_scalar(self):

        return self.layer_type == LayerType.SCALAR

    def is_vector(self):

        return self.layer_type in (
            LayerType.VECTOR2,
            LayerType.VECTOR3,
        )

    def is_material(self):

        return self.layer_type == LayerType.MATERIAL