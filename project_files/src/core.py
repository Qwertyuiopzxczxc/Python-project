"""
Слой бизнес-логики (Core).
Добавление, редактирование и удаление задач.
Версия: 0.2.0
"""

from typing import List, Dict, Any, Optional


def add_task(tasks: List[Dict[str, Any]], name: str, content: str) -> Optional[Dict[str, Any]]:
    """
    Добавляет новую задачу.
    Возвращает созданную задачу или None, если данные некорректны.
    """
    name = name.strip()
    content = content.strip()

    if not name:
        return None
    if not content:
        return None

    task = {
        "name": name,
        "content": content
    }
    tasks.append(task)
    return task


def edit_task(
    tasks: List[Dict[str, Any]],
    index: int,
    new_name: str,
    new_content: str
) -> bool:
    """
    Редактирует задачу по индексу (0-based).
    Возвращает True при успехе.
    """
    if not (0 <= index < len(tasks)):
        return False

    new_name = new_name.strip()
    new_content = new_content.strip()

    if not new_name or not new_content:
        return False

    tasks[index]["name"] = new_name
    tasks[index]["content"] = new_content
    return True


def delete_task(tasks: List[Dict[str, Any]], index: int) -> bool:
    """
    Удаляет задачу по индексу (0-based).
    Возвращает True при успехе.
    """
    if not (0 <= index < len(tasks)):
        return False
    tasks.pop(index)
    return True


def get_task_display_text(task: Dict[str, Any], number: int) -> str:
    """Формирует текст для отображения задачи в списке."""
    return f"{number}. {task['name']} — {task['content']}"