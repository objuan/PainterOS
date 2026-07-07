from painteros.canvas.dirty_manager import DirtyManager
from painteros.canvas.layer_manager import LayerManager
from painteros.canvas.statistics import CanvasStatistics
from painteros.canvas.tile_manager import TileManager
from painteros.canvas.transform_graph import TransformGraph


class CanvasState:

    def __init__(self):

        self.transforms = TransformGraph()

        self.tiles = TileManager()

        self.layers = LayerManager()

        self.statistics = CanvasStatistics()

        self.dirty = DirtyManager()