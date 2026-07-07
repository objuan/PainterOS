from painteros.canvas.tile_manager import TileManager
from painteros.math.rect import Rect


def test_create_tile():

    tm = TileManager(

        1000,

        1000,

        256,

    )

    t = tm.create_tile(0, 0)

    assert t.geometry.index.row == 0

    assert t.geometry.index.col == 0


def test_tile_at():

    tm = TileManager(

        1000,

        1000,

        256,

    )

    t = tm.tile_at(300, 100)

    assert t.geometry.index.col == 1


def test_tiles_in_rect():

    tm = TileManager(

        512,

        512,

        256,

    )

    r = Rect(

        0,

        0,

        300,

        300,

    )

    tiles = tm.tiles_in_rect(r)

    assert len(tiles) == 4


def test_clear():

    tm = TileManager(

        512,

        512,

    )

    tm.tile_at(10, 10)

    tm.clear()

    assert len(tm) == 0