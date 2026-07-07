from __future__ import annotations

from dataclasses import dataclass


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

    def contains(self, x: int, y: int):

        return (
            self.left <= x < self.right
            and
            self.top <= y < self.bottom
        )

    def area(self):

        return self.width * self.height