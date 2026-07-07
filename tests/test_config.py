from painteros.core.config import ConfigManager


def test_missing():
    c = ConfigManager("missing")
    assert c.get("x", 1) == 1
