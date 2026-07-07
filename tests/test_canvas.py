from painteros.canvas.brush import Brush
from painteros.canvas.state import CanvasState
from painteros.canvas.stroke import StrokeEngine


def test_stroke():
    s = CanvasState(50, 50)
    StrokeEngine().apply_point(s, 25, 25, Brush(), (1, 0, 0))
    assert s.layers.wetness.max() == 1.0
