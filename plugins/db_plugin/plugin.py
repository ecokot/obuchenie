from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .repository import UserRepository

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
        user_repository = UserRepository(sm)
        app.register_extension('db_session_factory', sm)
        app.register_extension('user_repository', user_repository)


    def startup(self):
        if self.config.create_tables:
            from .models import Base
            Base.metadata.create_all(self.engine)

    def shutdown(self):
        if self.engine is not None:
            self.engine.dispose()
