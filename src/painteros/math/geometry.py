from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Point:

    x: int
    y: int


@dataclass(slots=True)
class Size:

    width: int
    height: int


@dataclass(slots=True)
class Rect:

    x: int
    y: int

    width: int
    height: int

    @property
    def left(self):

        return self.x

    @property
    def right(self):

        return self.x + self.width

    @property
    def top(self):

        return self.y

    @property
    def bottom(self):

        return self.y + self.height

    def contains(
        self,
        x: int,
        y: int,
    ) -> bool:

        return (
            self.left <= x < self.right
            and
            self.top <= y < self.bottom
        )

    def intersects(
        self,
        other: "Rect",
    ) -> bool:

        return not (

            self.right <= other.left

            or

            self.left >= other.right

            or

            self.bottom <= other.top

            or

            self.top >= other.bottom

        )

    def union(
        self,
        other: "Rect",
    ) -> "Rect":

        x1 = min(self.left, other.left)

        y1 = min(self.top, other.top)

        x2 = max(self.right, other.right)

        y2 = max(self.bottom, other.bottom)

        return Rect(
            x1,
            y1,
            x2 - x1,
            y2 - y1,
        )

    @property
    def area(self):

        return self.width * self.height