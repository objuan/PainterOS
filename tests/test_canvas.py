'''
def test_stroke():

    canvas = CanvasState(

        50,

        50,

    )

    brush = Brush()

    StrokeEngine().apply_point(

        canvas,

        25,

        25,

        brush,

        (1,0,0),

    )

    tile = canvas.tiles.tile_at(

        25,

        25,

    )

    layer = tile.layer(

        "wetness"

    )

    assert layer.get(

        25,

        25,

    ) == 1.0
'''