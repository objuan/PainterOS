from .layers import CanvasLayers


class CanvasState:
    def __init__(self, w, h):
        self.layers = CanvasLayers(w, h)

    def clear(self):
        for v in vars(self.layers).values():
            try:
                v.fill(0)
            except:
                pass
