from __future__ import annotations

from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime

from painteros.core.asset_type import AssetType
from painteros.core.asset_state import AssetState


@dataclass(slots=True)
class Asset:

    name: str

    asset_type: AssetType

    uuid: str = field(default_factory=lambda: str(uuid4()))

    version: int = 1

    description: str = ""

    author: str = ""

    tags: set[str] = field(default_factory=set)

    metadata: dict = field(default_factory=dict)

    dependencies: list[str] = field(default_factory=list)

    created: datetime = field(default_factory=datetime.utcnow)

    modified: datetime = field(default_factory=datetime.utcnow)

    state: AssetState = AssetState.UNLOADED

    ref_count: int = 0

    def load(self):

        self.state = AssetState.LOADED

    def unload(self):

        self.state = AssetState.UNLOADED

    def mark_dirty(self):

        self.state = AssetState.DIRTY

    def add_reference(self):

        self.ref_count += 1

    def remove_reference(self):

        self.ref_count = max(0, self.ref_count - 1)