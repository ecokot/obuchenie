import logging
from typing import Protocol
from .app import App

logger = logging.getLogger(__name__)

class Plugin(Protocol):
    def register(self, app: App) -> None:
        ...

    def startup(self) -> None:
        ...

    def shutdown(self) -> None:
        ...


class PluginManager:
    def __init__(self, app: App) -> None:
        self.app = app

    def load_plugins(self):
        for plugin in self.app.plugins:
            try:
                plugin.register(self.app)
            except Exception as e:
                logger.error(f"Error loading plugins: {plugin.__class__.__name__} {e}")

    def startup(self):
        for plugin in self.app.plugins:
            try:
                plugin.startup()
            except Exception as e:
                logger.error(f"Error starting up plugins: {e}")

    def shutdown(self):
        for plugin in self.app.plugins:
            try:
                plugin.shutdown()
            except Exception as e:
                logger.error(f"Error shutting down plugins: {e}")