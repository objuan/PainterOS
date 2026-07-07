from enum import Enum, auto


class CoordinateSpace(Enum):

    ROBOT = auto()

    WORLD = auto()

    CANVAS = auto()

    TILE = auto()

    BRUSH = auto()