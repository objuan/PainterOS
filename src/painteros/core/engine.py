from __future__ import annotations

from painteros.core.engine_configuration import EngineConfiguration
from painteros.core.resource_manager import ResourceManager
from painteros.core.clock import SimulationClock

from painteros.surface.surface_state import SurfaceState


class PainterEngine:
    """
    Oggetto principale del motore.

    Coordina tutti i sottosistemi.
    """

    def __init__(

        self,

        config: EngineConfiguration,



    ):
        
        self.config=config

        self.clock = SimulationClock()

        self.resources = ResourceManager()

        self.surface = SurfaceState(

            config.canvas_width,

            config.canvas_height,

            config.tile_size,

        )

        # verranno implementati successivamente

        self.renderer = None

        self.physics = None

        self.robot = None

        self.vision = None

        self.ai = None

    def start(self):
        self.clock.start()

    def tick(

        self,

        dt: float,

    ):

        self.clock.tick(dt)

    def clear(self):

        self.surface.begin_frame()

        self.resources.clear()

    def update():
        pass
    '''
        dt = 1 / target_fps
        clock.tick(dt)

        physics.update(dt)
        brush_engine.update(dt)
        renderer.update(dt)
        robot.update(dt)
        vision.update(dt)
        '''