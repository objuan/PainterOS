from painteros.core.clock import SimulationClock


def test_tick():

    c = SimulationClock()

    c.start()

    c.tick(0.5)

    assert c.time == 0.5
