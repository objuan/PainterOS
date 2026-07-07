
from __future__ import annotations

from painteros.core.asset import Asset
from painteros.core.asset_type import AssetType


class Brush(Asset):
    """
    Brush base.

    Compatibile con le vecchie release e già predisposto
    per il Brush Engine.
    """

    def __init__(
        self,
        name: str = "Default Brush",
        radius: float = 10.0,
        hardness: float = 1.0,
        opacity: float = 1.0,
        flow: float = 1.0,
        spacing: float = 0.25,
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

    @property
    def diameter(self):

        return self.radius * 2.0