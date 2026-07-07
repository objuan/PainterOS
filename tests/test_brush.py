from painteros.brush.brush_tip import BrushTip
from painteros.brush.brush_state import BrushState
from painteros.brush.brush_stamp import BrushStamp
from painteros.brush.brush_asset import BrushAsset

def test_round_tip():

    tip = BrushTip(20)

    assert tip.mask.shape == (41, 41)

    assert tip.mask.max() == 1.0





def test_create():

    b = BrushAsset()

    assert b.radius == 10.0

    assert b.name == "Round Brush"

from painteros.brush.brush_state import BrushState


def test_state():

    state = BrushState(

        BrushAsset(),

    )

    assert state.radius() == 10.0


from painteros.brush.brush_tip import BrushTip


def test_mask():

    tip = BrushTip(

        BrushState(

            BrushAsset(),

        )

    )

    mask = tip.build_mask()

    assert mask.shape == (21, 21)