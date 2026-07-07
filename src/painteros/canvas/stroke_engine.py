import numpy as np


class StrokeEngine:
    def apply_path(self, state, points, brush, color):
        for (x0, y0), (x1, y1) in zip(points[:-1], points[1:], strict=False):
            steps = max(abs(x1 - x0), abs(y1 - y0), 1)
            for i in range(steps + 1):
                t = i / steps
                self.apply_point(
                    state, int(x0 + t * (x1 - x0)), int(y0 + t * (y1 - y0)), brush, color
                )

    def apply_point(self, state, x, y, brush, color):
        r = brush.radius
        yy, xx = np.ogrid[-r : r + 1, -r : r + 1]
        d = np.sqrt(xx * xx + yy * yy)
        w = np.exp(-(d * d) / (2 * (r / 2 + 0.1) ** 2)) * brush.opacity
        ys = slice(max(0, y - r), min(state.layers.pigment.shape[0], y + r + 1))
        xs = slice(max(0, x - r), min(state.layers.pigment.shape[1], x + r + 1))
        p = state.layers.pigment[ys, xs]
        wet = state.layers.wetness[ys, xs]
        ww = w[: p.shape[0], : p.shape[1]][..., None]
        p[:] = p * (1 - ww) + np.array(color, np.float32) * ww
        wet[:] = np.maximum(wet, w[..., 0] if ww.ndim == 3 else w[: wet.shape[0], : wet.shape[1]])
