class ResourceManager:
    def __init__(self):
        self._cache = {}

    def put(self, key, val):
        self._cache[key] = val

    def get(self, key, default=None):
        return self._cache.get(key, default)

    def clear(self):
        self._cache.clear()
