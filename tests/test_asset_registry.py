from painteros.core.asset import Asset
from painteros.core.asset_registry import AssetRegistry
from painteros.core.asset_type import AssetType


def test_register():

    r = AssetRegistry()

    a = Asset(

        name="Brush",

        asset_type=AssetType.BRUSH,

    )

    r.register(a)

    assert len(r) == 1


def test_find_name():

    r = AssetRegistry()

    a = Asset(

        "Paper",

        AssetType.MATERIAL,

    )

    r.register(a)

    assert r.find_name("Paper") is a


def test_find_type():

    r = AssetRegistry()

    a = Asset(

        "A",

        AssetType.BRUSH,

    )

    b = Asset(

        "B",

        AssetType.BRUSH,

    )

    r.register(a)

    r.register(b)

    assert len(

        r.find_type(

            AssetType.BRUSH

        )

    ) == 2


def test_find_tag():

    r = AssetRegistry()

    a = Asset(

        "Oil",

        AssetType.MATERIAL,

    )

    a.tags.add("paint")

    a.tags.add("oil")

    r.register(a)

    assert len(

        r.find_tag("oil")

    ) == 1


def test_unregister():

    r = AssetRegistry()

    a = Asset(

        "Brush",

        AssetType.BRUSH,

    )

    r.register(a)

    r.unregister(a.uuid)

    assert len(r) == 0