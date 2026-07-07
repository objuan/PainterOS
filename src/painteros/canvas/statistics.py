from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CanvasStatistics:
    """
    Runtime statistics of the canvas.
    """

    total_tiles: int = 0
    dirty_tiles: int = 0

    loaded_layers: int = 0

    modified_pixels: int = 0

    memory_bytes: int = 0

    rendered_frames: int = 0

    physics_frames: int = 0

    render_time_ms: float = 0.0

    physics_time_ms: float = 0.0

    def reset(self):

        self.total_tiles = 0
        self.dirty_tiles = 0

        self.loaded_layers = 0

        self.modified_pixels = 0

        self.memory_bytes = 0

        self.rendered_frames = 0

        self.physics_frames = 0

        self.render_time_ms = 0.0

        self.physics_time_ms = 0.0

    @property
    def memory_mb(self):

        return self.memory_bytes / 1024.0 / 1024.0

    def add_memory(self, value: int):

        self.memory_bytes += value

    def remove_memory(self, value: int):

        self.memory_bytes = max(
            0,
            self.memory_bytes - value,
        )

    def add_modified_pixels(self, pixels: int):

        self.modified_pixels += pixels

    def frame_rendered(self, elapsed_ms: float):

        self.rendered_frames += 1
        self.render_time_ms = elapsed_ms

    def frame_physics(self, elapsed_ms: float):

        self.physics_frames += 1
        self.physics_time_ms = elapsed_ms