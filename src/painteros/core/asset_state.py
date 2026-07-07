from enum import Enum, auto


class AssetState(Enum):

    UNLOADED = auto()

    LOADED = auto()

    DIRTY = auto()

    ERROR = auto()