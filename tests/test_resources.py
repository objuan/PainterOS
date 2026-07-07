from painteros.resources.manager import ResourceManager


def test_cache():
    r = ResourceManager()
    r.put("x", 5)
    assert r.get("x") == 5
