from .config import Config
import logging

logger = logging.getLogger(__name__)

class App:
    def __init__(self, config: Config):
        self.config = config
        self.extensions = {}
        self.plugins = []
        self.plugin_manager = None

    def add_plugin(self, plugin):
        if plugin not in self.plugins:
            self.plugins.append(plugin)
        else:
            logger.warning(f"Plugin {plugin.__class__.__name__} already added. Skipping...")

    def set_plugin_manager(self, pm):
        if self.plugin_manager is None:
            self.plugin_manager = pm
        else:
            raise RuntimeError("PluginManager already set")

    def start(self):
        if self.plugin_manager is None:
            raise RuntimeError("PluginManager not set")
        self.plugin_manager.startup()

    def stop(self):
        if self.plugin_manager is None:
            raise RuntimeError("PluginManager not set")
        self.plugin_manager.shutdown()