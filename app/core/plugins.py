import logging
from typing import Protocol
from .app import App

logger = logging.getLogger(__name__)

class Plugin(Protocol):
    def register(self, app: App) -> None:
        ...


class PluginManager:
    def __init__(self, plugins: list[Plugin], app: App) -> None:
        self.plugins = plugins
        self.app = app

    def load_plugins(self):
        for plugin in self.plugins:
            try:
                plugin.register(self.app)
            except Exception as e:
                logger.error(f"Error loading plugins: {plugin.__class__.__name__} {e}")