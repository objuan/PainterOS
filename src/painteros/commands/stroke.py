from __future__ import annotations

from dataclasses import dataclass, field

from uuid import UUID, uuid4

from .command import Command


@dataclass(slots=True)
class StrokeSample:

    x: float

    y: float

    pressure: float

    tilt_x: float

    tilt_y: float

    rotation: float

    speed: float


@dataclass(slots=True)
class StrokeCommand(Command):

    brush: str

    color: tuple[float, float, float]

    samples: list[StrokeSample] = field(default_factory=list)

    def execute(self, context):

        engine = context.get("stroke_engine")

        engine.execute(self)