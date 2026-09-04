# tests/test_plugin_manager.py
from app.core import App, Config
from app.core.plugins import PluginManager

class FakePlugin:
    def __init__(self):
        self.registered = False

    def register(self, app):
        self.registered = True  # ТВОЙ КОД: что изменить, чтобы тест заметил вызов?

def test_load_plugins_calls_register():
    config = Config()
    app = App(config)
    plugin_manager = PluginManager([FakePlugin()], app)
    plugin_manager.load_plugins()
    assert plugin_manager.plugins[0].registered == True
    ...  # ТВОЙ КОД: создай App, FakePlugin, PluginManager,
    # вызови load_plugins() и проверь assert, что register был вызван