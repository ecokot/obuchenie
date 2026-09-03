from app.core import App
import logging

logger = logging.getLogger(__name__)

class AuthPlugin:
    def register(self, app: App) -> None:
        logger.info(f"AuthPlugin подключен в {app.config.app_name}")