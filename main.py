from app.core import App, Config
from app.core.plugins import PluginManager
from plugins.auth import AuthPlugin
from dotenv import load_dotenv
import logging
import os


logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(name)s - %(message)s")

load_dotenv() # load .env file
config = Config(app_name=os.getenv("APP_NAME", "MiniPlatform"), debug=True)
app = App(config)
plugin_manager = PluginManager([AuthPlugin()], app)

plugin_manager.load_plugins()