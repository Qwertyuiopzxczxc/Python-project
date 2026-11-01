"""
Слой представления (View).
Методы для отображения задач.
Версия: 0.2.0
"""

from typing import List, Dict, Any
from core import get_task_display_text


def show_tasks(tasks: List[Dict[str, Any]]) -> None:
    """
    Выводит задачи в консоль (для отладки / совместимости).
    Основное отображение происходит через AppListbox в interface.py.
    """
    if not tasks:
        print("Список задач пуст.")
        return

    print("\n=== Список задач ===")
    for i, task in enumerate(tasks, start=1):
        print(get_task_display_text(task, i))
    print("====================\n")


def show_task_details(task: Dict[str, Any]) -> str:
    """Возвращает подробное описание задачи."""
    return f"Название: {task['name']}\nСодержимое: {task['content']}"