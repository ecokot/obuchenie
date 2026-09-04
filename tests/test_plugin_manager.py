# tests/test_plugin_manager.py
from app.core import App, Config
from app.core.plugins import PluginManager

class FakePlugin:
    def __init__(self):
        self.registered = False
    def register(self, app):
        self.registered = True

class BrokenPlugin:
    def __init__(self):
        self.registered = False

    def register(self, app):
        raise ValueError("This plugin is broken")



def test_load_plugins_calls_register():
    config = Config()
    app = App(config)
    plugin_manager = PluginManager([FakePlugin()], app)
    plugin_manager.load_plugins()
    assert plugin_manager.plugins[0].registered




def test_load_plugins_continues_after_error():
    config = Config()
    app = App(config)
    plugin_manager = PluginManager([BrokenPlugin(), FakePlugin()], app)
    plugin_manager.load_plugins()
    assert not plugin_manager.plugins[0].registered
    assert plugin_manager.plugins[1].registered