from app.core import App, Config
from app.core.plugins import PluginManager
from plugins.auth import AuthPlugin

config = Config()
app = App(config)
plugin_manager = PluginManager([AuthPlugin()],app)

plugin_manager.load_plugins()