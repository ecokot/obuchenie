from app.core import App
class AuthPlugin:
    def register(self, app: App) -> None:
        print("AuthPlugin подключен")