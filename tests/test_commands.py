from uuid import uuid4

from painteros.commands.stroke import StrokeCommand


def test_command():

    c = StrokeCommand(

        id=uuid4(),

        timestamp=0,

        brush="round",

        color=(1, 0, 0),

    )

    assert c.brush == "round"