from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@dataclass
class DBConfig:
    connection_string: str
    create_tables: bool = False
    echo: bool = False


class DBPlugin:
    def __init__(self, config: DBConfig):
        self.config = config
        self.app = None
        self.engine = None

    def register(self, app):
        if self.app is not None:
            raise RuntimeError("Plugin is already registered with an app")
        self.app = app
        self.engine = create_engine(self.config.connection_string, echo=self.config.echo)
        sm = sessionmaker(bind=self.engine)
        app.register_extension('db_session_factory', sm)

    def startup(self):
        ...

    def shutdown(self):
        if self.engine is not None:
            self.engine.dispose()
