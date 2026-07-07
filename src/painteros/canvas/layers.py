from dataclasses import dataclass

import numpy as np


@dataclass
class CanvasLayers:
    width: int
    height: int

    def __post_init__(self):
        s = (self.height, self.width)
        self.pigment = np.zeros((self.height, self.width, 3), dtype=np.float32)
        self.wetness = np.zeros(s, dtype=np.float32)
        self.thickness = np.zeros(s, dtype=np.float32)
        self.heightmap = np.zeros(s, dtype=np.float32)
