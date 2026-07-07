from dataclasses import dataclass


@dataclass(slots=True)
class SurfaceStatistics:

    total_tiles: int = 0

    loaded_tiles: int = 0

    dirty_tiles: int = 0

    modified_pixels: int = 0

    memory_bytes: int = 0

    render_time_ms: float = 0

    physics_time_ms: float = 0

    frame: int = 0

    @property
    def memory_mb(self):

        return self.memory_bytes / 1024 / 1024

    def next_frame(self):

        self.frame += 1