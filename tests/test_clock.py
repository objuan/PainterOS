from painteros.core.clock import SimulationClock


def test_tick():

    c = SimulationClock()

    c.start()

    c.tick(0.5)

    assert c.simulation_time == 0.5
    assert c.frame == 1


def test_pause():

    c = SimulationClock()

    c.start()

    c.pause()

    c.tick(1)

    assert c.simulation_time == 0


def test_step():

    c = SimulationClock()

    c.step(0.25)

    assert c.simulation_time == 0.25