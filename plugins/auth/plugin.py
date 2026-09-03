from app.core import App
class AuthPlugin:
    def register(self, app: App) -> None:
        print(f"AuthPlugin подключен в {app.config.app_name}")