from painteros.canvas.layer_manager import LayerManager
from painteros.canvas.layer import CanvasLayer


def test_add_layer():

    m = LayerManager()

    l = CanvasLayer("pigment", 3, "float32")

    m.add(l)

    assert len(m) == 1

    assert "pigment" in m


def test_remove():

    m = LayerManager()

    m.add(CanvasLayer("wetness", 1, "float32"))

    m.remove("wetness")

    assert len(m) == 0


def test_exists():

    m = LayerManager()

    m.add(CanvasLayer("height", 1, "float32"))

    assert m.exists("height")