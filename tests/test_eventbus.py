from painteros.core.eventbus import EventBus


def test_pub():
    b = EventBus()
    r = []
    b.subscribe("e", lambda x: r.append(x))
    b.publish("e", 5)
    assert r == [5]
