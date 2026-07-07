from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Point2D:
    x: float
    y: float

    def __add__(self, other: "Point2D") -> "Point2D":
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point2D") -> "Point2D":
        return Point2D(self.x - other.x, self.y - other.y)

    def scale(self, value: float) -> "Point2D":
        return Point2D(self.x * value, self.y * value)