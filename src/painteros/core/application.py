from __future__ import annotations

from painteros.application.context import ApplicationContext


class PainterApplication:
    """
    PainterOS main application.
    """

    def __init__(self) -> None:

        self.context = ApplicationContext()

        self.started = False

    def configure(self) -> None:
        """
        Configure all core services.
        """

    def start(self) -> None:

        if self.started:
            return

        self.configure()

        self.started = True

    def shutdown(self) -> None:

        self.context.services.clear()

        self.started = False