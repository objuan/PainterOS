from dataclasses import dataclass


@dataclass
class Brush:
    radius: int = 5
    pressure: float = 1.0
    opacity: float = 1.0
