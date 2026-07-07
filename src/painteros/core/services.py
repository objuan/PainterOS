class ServiceContainer:
    def __init__(self):
        self._s = {}

    def register(self, name, obj):
        self._s[name] = obj

    def resolve(self, name):
        return self._s[name]

    def has(self, name):
        return name in self._s
