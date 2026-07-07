import numpy as np


class DebugRenderer:
    def rgb(self, state):
        return (np.clip(state.layers.pigment, 0, 1) * 255).astype("uint8")

    def wetness(self, state):
        w = (np.clip(state.layers.wetness, 0, 1) * 255).astype("uint8")
        return np.stack([w, w, w], axis=-1)
