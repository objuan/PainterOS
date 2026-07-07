from __future__ import annotations

from dataclasses import dataclass

from painteros.math.transform2d import Transform2D
from painteros.canvas.spaces import CoordinateSpace


@dataclass(slots=True)
class TransformEdge:

    source: CoordinateSpace

    target: CoordinateSpace

    transform: Transform2D

class TransformGraph:

    def __init__(self):

        self._edges = {}

    def connect(

        self,

        source,

        target,

        transform,

    ):

        self._edges[(source, target)] = transform

    def get(

        self,

        source,

        target,

    ):

        return self._edges[(source, target)]