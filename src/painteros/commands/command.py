from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(slots=True)
class Command(ABC):

    id: UUID

    timestamp: float

    @abstractmethod
    def execute(self, context):
        ...