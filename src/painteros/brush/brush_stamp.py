from __future__ import annotations

import numpy as np

from painteros.brush.brush_tip import BrushTip
from painteros.brush.brush_state import BrushState


class BrushStamp:
    """
    Impronta fisica del pennello.
    """

    def __init__(
        self,
        state: BrushState,
    ):

        self.state = state

        self.tip = BrushTip(state)

    def pigment_mask(self):

        return (
            self.tip.mask
            * self.state.pigment
            * self.state.asset.opacity
        )

    def water_mask(self):

        return (
            self.tip.mask
            * self.state.water
        )

    def paint_mask(self):

        return (
            self.tip.mask
            * self.state.loaded_paint
        )