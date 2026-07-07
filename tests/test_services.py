from painteros.core.services import ServiceContainer


def test_register():
    s = ServiceContainer()
    s.register("a", 1)
    assert s.resolve("a") == 1
