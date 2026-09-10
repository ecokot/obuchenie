from dataclasses import dataclass

@dataclass
class DBConfig:
    connection_string: str
    create_tables: bool = False
    echo: bool = False


class DBPlugin:
    def __init__(self, config: DBConfig):
        self.config = config
        self.app = None

    def register(self, app):
        if self.app is not None:
            raise RuntimeError("Plugin is already registered with an app")
        self.app = app

    def startup(self):
        ...

    def shutdown(self):
        ...
