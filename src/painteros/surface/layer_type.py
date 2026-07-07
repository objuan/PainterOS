from __future__ import annotations

from enum import Enum, auto


class LayerType(Enum):
    """
    Tipo logico del layer.

    Determina come il renderer,
    il BrushEngine e la fisica
    interpreteranno i dati.
    """

    SCALAR = auto()

    VECTOR2 = auto()

    VECTOR3 = auto()

    SPECTRAL = auto()

    MASK = auto()

    INTEGER = auto()

    MATERIAL = auto()

    CUSTOM = auto()