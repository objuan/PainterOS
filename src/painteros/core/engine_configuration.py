from dataclasses import dataclass


@dataclass(slots=True)
class EngineConfiguration:

    canvas_width: int = 4000

    canvas_height: int = 3000

    tile_size: int = 256

    target_fps: int = 60

    enable_gpu: bool = False

    enable_ros2: bool = False

    enable_ai: bool = False

    enable_renderer: bool = True

    enable_physics: bool = True