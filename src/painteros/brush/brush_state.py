from __future__ import annotations

from dataclasses import dataclass

from painteros.brush.brush_asset import BrushAsset



class BrushState:
    """
    Stato runtime del pennello.
    """

    def __init__(

        self,

        asset=None,

    ):

        if asset is None:

            asset = BrushAsset()

        self.asset = asset

        self.pressure = 1.0

        self.speed = 0.0

        self.tilt = 0.0

        self.rotation = 0.0

        self.pigment = 1.0

        self.water = 1.0

    def radius(self):

        return self.asset.radius * self.pressure

    def reset(self):

        self.pressure = 1.0
        self.speed = 0.0
        self.tilt = 0.0
        self.rotation = 0.0
        self.pigment = 1.0
        self.water = 1.0
        self.loaded_paint = 1.0