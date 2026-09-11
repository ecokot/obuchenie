# Проект MiniPlatform — Структура и Описание

## 📋 Обзор

**MiniPlatform** — это легковесная модульная платформа на Python с архитектурой на основе плагинов. Проект предназначен для обучения работе с:

- Плагин-ориентированной архитектурой (Plugin-based Architecture)
- Паттернами проектирования (Protocol, Factory, Dependency Injection)
- SQLAlchemy (ORM для SQL-баз данных)
- FastAPI (асинхронный веб-фреймворк)
- Асинхронным программированием (async/await)

---

## 📁 Структура проекта

```
obuchenie/
├── main.py                     # Точка входа в приложение
├── requirements.txt            # Зависимости проекта
├── plan.txt                    # План работ / заметки
├── PROJECT_STRUCTURE.md        # Этот файл
│
├── app/                        # Ядро приложения
│   ├── __init__.py
│   └── core/
│       ├── __init__.py
│       ├── app.py              # Класс App — основное приложение
│       ├── config.py           # Конфигурация (Config dataclass)
│       └── plugins.py          # PluginManager + Protocol Plugin
│
├── plugins/                    # Плагины
│   ├── __init__.py
│   ├── auth/
│   │   ├── __init__.py
│   │   └── plugin.py           # AuthPlugin — плагин аутентификации
│   └── db_plugin/
│       ├── __init__.py
│       └── plugin.py           # DBPlugin — плагин работы с БД (SQLAlchemy)
│
├── demo/                       # Демонстрационные скрипты
│   ├── async_demo.py           # Демонстрация async/await
│   ├── cm_demo.py              # Демонстрация контекстных менеджеров
│   ├── db_demo.py              # Демонстрация работы с БД
│   ├── fastapi_demo.py         # Демонстрация FastAPI интеграции
│   ├── load_test.py            # Нагрузочное тестирование
│   ├── repository_demo.py      # Демонстрация паттерна Repository
│   ├── sqlalchemy_demo.py      # Базовая работа с SQLAlchemy
│   ├── sqlalchemy_async_demo.py # Асинхронный SQLAlchemy
│   ├── sqlalchemy_model_demo.py # Демонстрация моделей SQLAlchemy
│   ├── sqlalchemy_relationship_demo.py # Отношения между моделями
│   └── sqlalchemy_session_demo.py   # Управление сессиями SQLAlchemy
│
├── tests/                      # Тесты
│   ├── test_app.py             # Тесты ядра приложения
│   └── test_plugin_manager.py  # Тесты PluginManager
│
└── .env                        # (опционально) Переменные окружения
```

---

## 🧱 Компоненты ядра

### 1. `app/core/config.py` — Конфигурация

```python
@dataclass
class Config:
    app_name: str = "MiniPlatform"   # Имя приложения
    debug: bool = False               # Режим отладки
```

- Простой dataclass для хранения настроек
- Загружается из `.env` через `python-dotenv`

---

### 2. `app/core/app.py` — Класс `App`

Основной класс приложения, реализующий центральный хаб:

| Метод | Описание |
|-------|----------|
| `__init__(config)` | Инициализация с конфигурацией |
| `add_plugin(plugin)` | Добавление плагина |
| `set_plugin_manager(pm)` | Установка менеджера плагинов |
| `register_extension(key, value)` | Регистрация расширения (DI) |
| `get_extension(key)` | Получение расширения |
| `start()` | Запуск всех плагинов |
| `stop()` | Остановка всех плагинов |

**Хранилища:**
- `self.extensions` — словарь зарегистрированных расширений (DI-контейнер)
- `self.plugins` — список активных плагинов
- `self.plugin_manager` — ссылка на PluginManager

---

### 3. `app/core/plugins.py` — PluginManager и Protocol

**Protocol `Plugin`:**
```python
class Plugin(Protocol):
    def register(app: App) -> None: ...   # Регистрация в приложении
    def startup(app: App) -> None: ...     # Инициализация при старте
    def shutdown(app: App) -> None: ...    # Очистка при остановке
```

**Класс `PluginManager`:**
- Управляет жизненным циклом плагинов
- Вызывает `register()`, `startup()`, `shutdown()` для каждого плагина
- Обрабатывает исключения, не допуская падения приложения

---

## 🔌 Плагины

### `plugins/auth/plugin.py` — AuthPlugin

Плагин для аутентификации. На данном этапе — заглушка для демонстрации структуры.

```python
class AuthPlugin:
    def register(self, app: App) -> None:
        logger.info(f"AuthPlugin подключен в {app.config.app_name}")
```

---

### `plugins/db_plugin/plugin.py` — DBPlugin

Плагин для работы с базами данных через SQLAlchemy:

```python
@dataclass
class DBConfig:
    connection_string: str   # DSN базы данных
    create_tables: bool = False
    echo: bool = False

class DBPlugin:
    def register(self, app: App):
        # Создаёт engine и sessionmaker
        # Регистрирует sessionmaker в DI-контейнере под ключом 'db_session_factory'

    def startup(self):
        # Инициализация при старте

    def shutdown(self):
        # Закрытие соединений с БД
```

**Использование:**
```python
db_plugin = DBPlugin(DBConfig("sqlite:///app.db", echo=True))
plugin_manager.load_plugin(db_plugin)
```

---

## 🚀 Точка входа

### `main.py`

```python
load_dotenv()
config = Config(
    app_name=os.getenv("APP_NAME", "MiniPlatform"),
    debug=os.getenv("DEBUG", "False").lower() == "true"
)

app = App(config)
plugin_manager = PluginManager(app)
app.set_plugin_manager(plugin_manager)
plugin_manager.load_plugins()
```

---

## 📦 Демонстрации (`demo/`)

| Файл | Тема |
|------|------|
| `async_demo.py` | Основы async/await в Python |
| `cm_demo.py` | Контекстные менеджеры (`with` statements) |
| `db_demo.py` | Работа с базами данных |
| `fastapi_demo.py` | Интеграция с FastAPI |
| `load_test.py` | Нагрузочное тестирование |
| `repository_demo.py` | Паттерн Repository |
| `sqlalchemy_demo.py` | Базовый SQLAlchemy |
| `sqlalchemy_async_demo.py` | Асинхронный SQLAlchemy (aiomysql/asyncpg) |
| `sqlalchemy_model_demo.py` | Определение моделей |
| `sqlalchemy_relationship_demo.py` | Отношения (1:N, N:N) |
| `sqlalchemy_session_demo.py` | Управление сессиями |

---

## 🧪 Тесты (`tests/`)

| Файл | Что тестирует |
|------|---------------|
| `test_app.py` | Ядро приложения (`App`) |
| `test_plugin_manager.py` | Менеджер плагинов (`PluginManager`) |

**Запуск:**
```bash
pytest
```

---

## 📦 Зависимости (`requirements.txt`)

| Пакет | Версия | Назначение |
|-------|--------|------------|
| `python-dotenv` | >=1.2.3 | Загрузка переменных из `.env` |
| `SQLAlchemy` | ~=2.0.52 | ORM для работы с БД |
| `fastapi` | >=0.115.0 | Веб-фреймворк |
| `pydantic` | >=2.0.0 | Валидация данных |
| `aiosqlite` | >=0.20.0 | Асинхронный SQLite |
| `uvicorn` | >=0.30.0 | ASGI-сервер |
| `pytest` | >=8.0.0 | Фреймворк тестирования |
| `greenlet` | >=3.0.0 | Поддержка async |

---

## 🏗 Архитектурные паттерны

1. **Plugin Architecture** — модульность через плагины
2. **Dependency Injection** — расширения регистрируются в `app.extensions`
3. **Protocol-Oriented Design** — `Plugin` как structural protocol
4. **Lifecycle Management** — `register → startup → shutdown`
5. **Configuration via Dataclass** — типобезопасная конфигурация

---

## ▶️ Запуск

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск приложения
python main.py

# Запуск тестов
pytest

# Запуск демонстрации FastAPI
python demo/fastapi_demo.py
```

---

## 📝 Примечания

- Проект является обучающим и демонстрирует различные паттерны и технологии Python
- Плагины реализуют structural `Protocol`, что позволяет использовать их без явного наследования
- Для продакшена требуется расширение `AuthPlugin` и добавление реальной логики аутентификации
