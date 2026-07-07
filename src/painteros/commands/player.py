from __future__ import annotations

from .recorder import CommandRecorder


class CommandPlayer:

    def play(

        self,

        recorder: CommandRecorder,

        context,

    ):

        for command in recorder:

            command.execute(context)