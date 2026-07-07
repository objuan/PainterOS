from painteros.core.services import ServiceContainer


def test_singleton():

    c = ServiceContainer()

    obj = object()

    c.register_singleton("obj", obj)

    assert c.resolve("obj") is obj


def test_factory():

    c = ServiceContainer()

    c.register_factory("number", lambda: 42)

    assert c.resolve("number") == 42


def test_remove():

    c = ServiceContainer()

    c.register_singleton("a", 5)

    c.remove("a")

    assert not c.has("a")