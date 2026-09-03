from typing import Protocol
from .app import App

class Plugin(Protocol):
    def register(self, app: App) -> None:
        ...


class PluginManager:
    def __init__(self, plugins: list[Plugin], app: App) -> None:
        self.plugins = plugins
        self.app = app

    def load_plugins(self):
        for plugin in self.plugins:
            plugin.register(self.app)
