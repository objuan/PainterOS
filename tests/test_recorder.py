from uuid import uuid4

from painteros.commands.recorder import CommandRecorder

from painteros.commands.stroke import StrokeCommand


def test_record():

    r = CommandRecorder()

    cmd = StrokeCommand(

        id=uuid4(),

        timestamp=0,

        brush="round",

        color=(1, 0, 0),

    )

    r.record(cmd)

    assert len(r) == 1