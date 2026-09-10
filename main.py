from app.core import App, Config
from app.core.plugins import PluginManager
from dotenv import load_dotenv
import logging
import os

load_dotenv()
config = Config(app_name=os.getenv("APP_NAME", "MiniPlatform"), debug=os.getenv("DEBUG", "False").lower() == "true")

if config.debug:
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(name)s - %(message)s")
else:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(name)s - %(message)s")


app = App(config)
plugin_manager = PluginManager(app)
app.set_plugin_manager(plugin_manager)
plugin_manager.load_plugins()