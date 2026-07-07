from painteros.surface.storage.numpy_storage import NumpyStorage


def test_storage():

    s = NumpyStorage(

        128,

        128,

        1,

        float,

        0,

    )

    s.set(

        20,

        30,

        7,

    )

    assert s.get(

        20,

        30,

    ) == 7