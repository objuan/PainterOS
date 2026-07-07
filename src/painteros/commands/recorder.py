from __future__ import annotations

from collections.abc import Iterator

from .command import Command


class CommandRecorder:

    def __init__(self):

        self._commands: list[Command] = []

    def record(self, command: Command):

        self._commands.append(command)

    def clear(self):

        self._commands.clear()

    def __len__(self):

        return len(self._commands)

    def __iter__(self) -> Iterator[Command]:

        return iter(self._commands)

    @property
    def commands(self):

        return tuple(self._commands)