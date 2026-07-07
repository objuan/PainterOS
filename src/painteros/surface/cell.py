from __future__ import annotations

from dataclasses import dataclass

from painteros.surface.material import Material


@dataclass(slots=True)
class Cell:

    """
    Singolo elemento fisico della superficie.

    Tutta la simulazione agirà su questa classe.
    """

    material: Material

    dirty: bool = False

    selected: bool = False

    last_frame: int = 0

    def mark_dirty(self, frame: int):

        self.dirty = True

        self.last_frame = frame