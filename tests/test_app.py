# tests/test_app.py
from app.core import App, Config

def test_app_stores_config():
    config = Config(app_name="Test")  # 1. создали объект
    app = App(config)                 # 2. действие — передали config в App
    assert app.config is config       # 3. проверка: App сохранил ТОТ ЖЕ объект


