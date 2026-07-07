import numpy as np


class StrokeEngine:
    def apply_point(self, state, x, y, brush, color):
        r = brush.radius
        yy, xx = np.ogrid[-r : r + 1, -r : r + 1]
        mask = xx * xx + yy * yy <= r * r
        ys = slice(max(0, y - r), min(state.layers.pigment.shape[0], y + r + 1))
        xs = slice(max(0, x - r), min(state.layers.pigment.shape[1], x + r + 1))
        sub = state.layers.pigment[ys, xs]
        m = mask[: sub.shape[0], : sub.shape[1]]
        sub[m] = np.array(color, dtype=np.float32)
        state.layers.wetness[ys, xs][m] = 1.0
