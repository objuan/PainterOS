from painteros.surface.layer_descriptor import LayerDescriptor
from painteros.surface.layer_type import LayerType


def test_descriptor():

    d = LayerDescriptor(

        name="water",

        layer_type=LayerType.SCALAR,

    )

    assert d.name == "water"

    assert d.is_scalar()

    assert not d.is_material()