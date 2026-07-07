from painteros.math.geometry import Rect


def test_contains():

    r = Rect(10, 10, 100, 100)

    assert r.contains(20, 20)

    assert not r.contains(200, 200)


def test_intersects():

    a = Rect(0, 0, 100, 100)

    b = Rect(50, 50, 20, 20)

    assert a.intersects(b)


def test_union():

    a = Rect(0, 0, 10, 10)

    b = Rect(10, 10, 10, 10)

    c = a.union(b)

    assert c.width == 20

    assert c.height == 20