from __future__ import annotations

import numpy as np

from painteros.brush.brush_state import BrushState
from painteros.brush.brush_asset import BrushAsset

class BrushTip:
    """
    Geometria istantanea della punta.
    """

    def __init__(self, state_or_radius):

        if isinstance(state_or_radius, BrushState):

            self.state = state_or_radius
            radius = int(self.state.radius())

        else:

            radius = int(state_or_radius)

            self.state = BrushState(
                BrushAsset(radius=radius)
            )

        self.radius = radius

        self.mask = self.build_mask()
        

    def build_mask(self):

        r = int(self.state.radius())

        size = r * 2 + 1

        y, x = np.ogrid[-r:r + 1, -r:r + 1]

        distance = np.sqrt(x * x + y * y)

        mask = np.clip(
            1.0 - distance / r,
            0.0,
            1.0,
        )

        return mask.astype(np.float32)