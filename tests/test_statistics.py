from painteros.canvas.statistics import CanvasStatistics


def test_memory():

    s = CanvasStatistics()

    s.add_memory(1024)

    assert s.memory_bytes == 1024


def test_remove_memory():

    s = CanvasStatistics()

    s.add_memory(5000)

    s.remove_memory(1000)

    assert s.memory_bytes == 4000


def test_modified_pixels():

    s = CanvasStatistics()

    s.add_modified_pixels(150)

    s.add_modified_pixels(200)

    assert s.modified_pixels == 350


def test_render():

    s = CanvasStatistics()

    s.frame_rendered(10.5)

    assert s.rendered_frames == 1

    assert s.render_time_ms == 10.5


def test_reset():

    s = CanvasStatistics()

    s.add_memory(500)

    s.add_modified_pixels(50)

    s.reset()

    assert s.memory_bytes == 0

    assert s.modified_pixels == 0