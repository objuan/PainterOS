from __future__ import annotations

from painteros.surface.cell import Cell
from painteros.surface.material import Material


class CellGrid:

    def __init__(

        self,

        size: int,

    ):

        self.size = size

        self.cells = [

            [

                Cell(Material())

                for _ in range(size)

            ]

            for _ in range(size)

        ]

    def cell(

        self,

        x: int,

        y: int,

    ) -> Cell:

        return self.cells[y][x]

    def clear(self):

        for row in self.cells:

            for cell in row:

                cell.material = Material()

                cell.dirty = False