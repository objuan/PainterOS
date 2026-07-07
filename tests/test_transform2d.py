from painteros.math.point import Point2D
from painteros.math.transform2d import Transform2D


def test_translation():

    t=Transform2D()

    t.translate(10,20)

    p=t.map(Point2D(1,2))

    assert p.x==11

    assert p.y==22


def test_scale():

    t=Transform2D()

    t.scale(2,3)

    p=t.map(Point2D(5,5))

    assert p.x==10

    assert p.y==15