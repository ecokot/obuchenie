# tests/test_plugin_manager.py
from app.core import App, Config
from app.core.plugins import PluginManager

class FakePlugin:
    def __init__(self):
        self.registered = False

    def register(self, app):
        ...  # ТВОЙ КОД: что изменить, чтобы тест заметил вызов?

def test_load_plugins_calls_register():
    ...  # ТВОЙ КОД: создай App, FakePlugin, PluginManager,
    # вызови load_plugins() и проверь assert, что register был вызван