from __future__ import annotations

from painteros.core.storage_manager import StorageManager
from painteros.core.asset_registry import AssetRegistry


class ResourceManager:

    def __init__(self):

        self.storage = StorageManager()

        self.assets = AssetRegistry()

    def clear(self):

        self.storage.clear()

        self.assets.clear()

   