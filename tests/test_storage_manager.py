from painteros.core.storage_manager import StorageManager
from painteros.surface.storage.numpy_storage import NumpyStorage


def test_register():

    s = StorageManager()

    st = NumpyStorage(

        10,

        10,

        1,

        float,

        0,

    )

    s.register(

        "main",

        st,

    )

    assert len(s) == 1