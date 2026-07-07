from __future__ import annotations

from dataclasses import dataclass, field
from painteros.core.old.asset import Asset
from painteros.core.asset_type import AssetType

import numpy as np


@dataclass(slots=True)
class Material(Asset):

    def __init__(self, name):

        super().__init__(

            name=name,

            asset_type=AssetType.MATERIAL,

        )
    """
    Proprietà fisiche di una cella.

    Questa classe NON rappresenta un pixel RGB,
    ma un materiale pittorico.
    """

    pigments: np.ndarray = field(
        default_factory=lambda: np.zeros(
            16,
            dtype=np.float32,
        )
    )

    water: float = 0.0

    binder: float = 0.0

    thickness: float = 0.0

    temperature: float = 20.0

    drying: float = 0.0

    absorbency: float = 0.5

    opacity: float = 1.0

    roughness: float = 0.0

    def reset(self):

        self.pigments.fill(0)

        self.water = 0.0

        self.binder = 0.0

        self.thickness = 0.0

        self.temperature = 20.0

        self.drying = 0.0

        self.absorbency = 0.5

        self.opacity = 1.0

        self.roughness = 0.0