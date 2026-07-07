from .services import ServiceContainer


class ApplicationContext:
    def __init__(self):
        self.services = ServiceContainer()
