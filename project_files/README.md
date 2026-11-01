# Task Manager — Develop-App Course

**Урок 13–14: Слоистая архитектура**

Простое приложение для управления задачами на Python + Tkinter.

## Структура проекта (слои)

```
TaskManager/
├── src/
│   ├── main.py              # Точка входа
│   ├── config.py            # Конфигурация
│   ├── storage.py           # Слой хранения (JSON)
│   ├── core.py              # Бизнес-логика
│   ├── view.py              # Методы отображения
│   ├── utils.py             # Вспомогательные функции
│   └── ui/
│       ├── interface.py     # Сборка интерфейса
│       ├── AppButton.py     # Кастомная кнопка
│       ├── AppLabel.py      # Кастомная метка
│       ├── AppListbox.py    # Кастомный список задач
│       └── AppFrame.py      # Кастомный фрейм
├── saves.json               # Файл сохранения
├── BACKLOG.md               # Список улучшений
├── BUGFIX.md                # Список исправлений
└── README.md
```

## Запуск

```bash
cd src
python main.py
```

Требуется Python 3.10+ (используется `int | None`).

## Выполненные требования ДЗ

- [x] `view.py`, `interface.py`, `storage.py`, `AppButton.py`
- [x] Сохранение в **JSON** вместо txt
- [x] Класс `AppLabel.py`
- [x] Отображение задач через `AppListbox.py`
- [x] `BACKLOG.md` заполнен
- [x] `BUGFIX.md` заполнен

## Автор

Develop-App Course • 2026
