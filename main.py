from app.core import App, Config
from app.core.plugins import PluginManager
from plugins.auth import AuthPlugin
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(name)s - %(message)s")

config = Config(app_name="FRMWQwen", debug=True)
app = App(config)
plugin_manager = PluginManager([AuthPlugin()], app)

plugin_manager.load_plugins()