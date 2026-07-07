from painteros.canvas.dirty_manager import DirtyManager
from painteros.math.rect import Rect


def test_add_region():

    d = DirtyManager()

    d.add(

        "pigment",

        0,

        0,

        Rect(0, 0, 10, 10),

        1,

    )

    assert len(d) == 1


def test_clear():

    d = DirtyManager()

    d.add(

        "pigment",

        0,

        0,

        Rect(0, 0, 10, 10),

        1,

    )

    d.clear()

    assert len(d) == 0


def test_layer_filter():

    d = DirtyManager()

    d.add(

        "pigment",

        0,

        0,

        Rect(0, 0, 5, 5),

        1,

    )

    d.add(

        "wetness",

        0,

        0,

        Rect(0, 0, 5, 5),

        1,

    )

    assert len(d.layer_regions("pigment")) == 1