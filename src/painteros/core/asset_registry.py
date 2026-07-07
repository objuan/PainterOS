from __future__ import annotations

from collections import defaultdict
from typing import Dict, Iterable, Iterator

from painteros.core.asset import Asset
from painteros.core.asset_type import AssetType


class AssetRegistry:
    """
    Registro centrale di tutti gli Asset del motore.

    Ogni Asset viene indicizzato per:

        • UUID
        • Nome
        • Tipo
        • Tag

    Tutti i manager accederanno a questo registry.
    """

    def __init__(self):

        self._assets: Dict[str, Asset] = {}

        self._name_index: Dict[str, str] = {}

        self._type_index = defaultdict(set)

        self._tag_index = defaultdict(set)

    # ---------------------------------------------------------

    def register(
        self,
        asset: Asset,
    ):

        if asset.uuid in self._assets:
            raise ValueError(
                f"Asset '{asset.uuid}' already registered."
            )

        self._assets[asset.uuid] = asset

        self._name_index[asset.name] = asset.uuid

        self._type_index[
            asset.asset_type
        ].add(asset.uuid)

        for tag in asset.tags:

            self._tag_index[tag].add(
                asset.uuid
            )

    # ---------------------------------------------------------

    def unregister(
        self,
        uuid: str,
    ):

        asset = self._assets.pop(uuid)

        self._name_index.pop(
            asset.name,
            None,
        )

        self._type_index[
            asset.asset_type
        ].discard(uuid)

        for tag in asset.tags:

            self._tag_index[tag].discard(
                uuid
            )

    # ---------------------------------------------------------

    def get(
        self,
        uuid: str,
    ) -> Asset:

        return self._assets[uuid]

    # ---------------------------------------------------------

    def find_name(
        self,
        name: str,
    ) -> Asset | None:

        uuid = self._name_index.get(name)

        if uuid is None:
            return None

        return self._assets[uuid]

    # ---------------------------------------------------------

    def find_type(
        self,
        asset_type: AssetType,
    ) -> list[Asset]:

        return [

            self._assets[x]

            for x in self._type_index[asset_type]

        ]

    # ---------------------------------------------------------

    def find_tag(
        self,
        tag: str,
    ) -> list[Asset]:

        return [

            self._assets[x]

            for x in self._tag_index[tag]

        ]

    # ---------------------------------------------------------

    def exists(
        self,
        uuid: str,
    ) -> bool:

        return uuid in self._assets

    # ---------------------------------------------------------

    def clear(self):

        self._assets.clear()

        self._name_index.clear()

        self._type_index.clear()

        self._tag_index.clear()

    # ---------------------------------------------------------

    @property
    def count(self):

        return len(self._assets)

    # ---------------------------------------------------------

    def assets(self) -> Iterable[Asset]:

        return self._assets.values()

    # ---------------------------------------------------------

    def uuids(self):

        return tuple(
            self._assets.keys()
        )

    # ---------------------------------------------------------

    def names(self):

        return tuple(
            self._name_index.keys()
        )

    # ---------------------------------------------------------

    def statistics(self):

        return {

            "assets": len(self._assets),

            "types": len(self._type_index),

            "tags": len(self._tag_index),

        }

    # ---------------------------------------------------------

    def __len__(self):

        return len(self._assets)

    # ---------------------------------------------------------

    def __contains__(self, uuid):

        return uuid in self._assets

    # ---------------------------------------------------------

    def __iter__(self) -> Iterator[Asset]:

        return iter(
            self._assets.values()
        )