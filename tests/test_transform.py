from painteros.math.point import Point2D
from painteros.math.transform import CoordinateTransform


def test_conversion():

    tr = CoordinateTransform(

        4000,
        3000,

        400,
        300,

    )

    w = Point2D(100, 50)

    c = tr.world_to_canvas(w)

    w2 = tr.canvas_to_world(c)

    assert abs(w.x - w2.x) < 0.001

    assert abs(w.y - w2.y) < 0.001