import numpy as np

from painteros.surface.layer_descriptor import LayerDescriptor
from painteros.surface.layer_type import LayerType
from painteros.surface.tile_layer import TileLayer


def test_create():

    d = LayerDescriptor(

        "water",

        LayerType.SCALAR,

    )

    l = TileLayer(

        d,

        256,

    )

    assert l.shape == (256, 256)


def test_set():

    d = LayerDescriptor(

        "water",

        LayerType.SCALAR,

    )

    l = TileLayer(

        d,

        128,

    )

    l.set(

        10,

        20,

        4.5,

    )

    assert np.isclose(

        l.get(10, 20),

        4.5,

    )


def test_clear():

    d = LayerDescriptor(

        "water",

        LayerType.SCALAR,

    )

    l = TileLayer(

        d,

        64,

    )

    l.set(

        0,

        0,

        7,

    )

    l.clear()

    assert l.get(0, 0) == 0