from __future__ import annotations

from dataclasses import dataclass

from painteros.math.point import Point2D


@dataclass(slots=True)
class CoordinateTransform:
    """
    Conversione tra World Space (mm) e Canvas Space (pixel).
    """

    canvas_width_px: int
    canvas_height_px: int

    canvas_width_mm: float
    canvas_height_mm: float

    @property
    def pixel_size_x(self):

        return self.canvas_width_mm / self.canvas_width_px

    @property
    def pixel_size_y(self):

        return self.canvas_height_mm / self.canvas_height_px

    def world_to_canvas(self, point: Point2D) -> Point2D:

        return Point2D(
            point.x / self.pixel_size_x,
            point.y / self.pixel_size_y,
        )

    def canvas_to_world(self, point: Point2D) -> Point2D:

        return Point2D(
            point.x * self.pixel_size_x,
            point.y * self.pixel_size_y,
        )