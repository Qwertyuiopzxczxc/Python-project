# Менеджер задач v0.2.0

Модульное приложение для управления списком задач на Python (`tkinter`), реализованное с использованием ООП и паттерна **Фасад (Facade)**.

## Структура проекта

* `task.py` — класс `Task` (модель данных задачи с сериализацией `to_dict()` и `from_dict()`).
* `storage_manager.py` — класс `StorageManager` (чтение и сохранение задач в `tasks.json`, методы `load`, `save`, `add`, `update`, `delete`).
* `components.py` — кастомные UI-виджеты (`AppLabel`, `AppEntry`, `AppButton`, `AppListbox`, `AppFrame`), унаследованные от виджетов `tkinter`.
* `interface.py` — класс `Interface` (прослойка графического интерфейса).
* `task_manager.py` — класс-фасад `TaskManager` (связывает хранилище и интерфейс, реализует CRUD-логику).
* `main.py` — точка входа в приложение.

## Запуск

```bash
python main.py
```
