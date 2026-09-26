from app.core import App
import logging

logger = logging.getLogger(__name__)

class AuthPlugin:
    def __init__(self):
        self.app = None
        self.user_repository = None

    def register(self, app: App):
        if self.app is not None:
            raise RuntimeError("Plugin is already registered with an app")
        self.app = app

    def startup(self):
        if self.app is None:
            raise RuntimeError("Plugin must be registered before startup")
        if self.user_repository is not None:
            raise RuntimeError("Plugin is already started")
        self.user_repository = self.app.get_extension('user_repository')

    def shutdown(self):
        ...

    def register_user(self, username:str, password:str):
        ...

    def authenticate(self, username:str, password:str):
        ...