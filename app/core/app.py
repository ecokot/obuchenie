from .config import Config
import logging

logger = logging.getLogger(__name__)

class App:
    def __init__(self, config: Config):
        self.config = config
        self.extensions = {}
        self.plugins = []

    def add_plugin(self, plugin):
        if plugin not in self.plugins:
            self.plugins.append(plugin)
        else:
            logger.warning(f"Plugin {plugin.__class__.__name__} already added. Skipping...")

    def start(self):
        ...

    def stop(self):
        ...