from __future__ import annotations

import json

from dataclasses import asdict

from .stroke import StrokeCommand


class CommandSerializer:

    @staticmethod
    def save(command: StrokeCommand, filename: str):

        with open(filename, "w", encoding="utf8") as fp:

            json.dump(
                asdict(command),
                fp,
                indent=4,
                default=str,
            )