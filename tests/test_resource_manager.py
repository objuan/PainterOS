from painteros.core.resource_manager import ResourceManager


def test_create():

    r = ResourceManager()

    assert len(r.assets) == 0
    assert len(r.storage) == 0