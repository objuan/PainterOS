from painteros.core.engine import PainterEngine
from painteros.core.engine_configuration import EngineConfiguration


def test_create():

    engine = PainterEngine(

      EngineConfiguration()

    )

    assert engine.surface is not None

    assert engine.resources is not None

    assert engine.clock is not None


def test_tick():

    engine = PainterEngine(

        EngineConfiguration()

    )

    engine.start()
    engine.tick(0.5)

    assert engine.clock.time == 0.5



def test_clear():

    engine = PainterEngine(

      EngineConfiguration()

    )

    engine.clear()

    assert len(engine.resources.assets) == 0