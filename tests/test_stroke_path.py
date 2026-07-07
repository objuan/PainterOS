from painteros.canvas.brush import Brush
from painteros.canvas.state import CanvasState
from painteros.canvas.stroke_engine import StrokeEngine


def test_path():
    s = CanvasState(100, 100)
    StrokeEngine().apply_path(s, [(10, 10), (90, 90)], Brush(radius=3, opacity=0.5), (1, 0, 0))
    assert s.layers.wetness.sum() > 0
