from __future__ import annotations

from dataclasses import dataclass

from painteros.core.asset import Asset
from painteros.core.asset_type import AssetType
from painteros.brush.brush_shape import BrushShape



class BrushAsset(Asset):
    """
    Definizione permanente di un pennello.
    Non cambia durante la simulazione.
    """

    radius: float = 10.0
    hardness: float = 0.8
    opacity: float = 1.0
    flow: float = 1.0
    spacing: float = 0.20

    shape: BrushShape = BrushShape.ROUND

    bristle_count: int = 1000

    elasticity: float = 0.7

    absorbency: float = 0.8

    def __init__(
        self,
        name: str = "Round Brush",
        radius=10,

        hardness=0.8,

        opacity=1.0,

        flow=1.0,

        spacing=0.2,
    ):

        super().__init__(
            name=name,
            asset_type=AssetType.BRUSH,
        )

        self.radius = radius
        self.hardness = hardness
        self.opacity = opacity
        self.flow = flow
        self.spacing = spacing
        self.shape = BrushShape.ROUND
        self.bristle_count = 1000
        self.elasticity = 0.7
        self.absorbency = 0.8