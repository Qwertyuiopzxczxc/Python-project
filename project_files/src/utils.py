"""
Вспомогательные функции.
Версия: 0.2.0
"""

import os
import sys


def get_base_dir() -> str:
    """Возвращает директорию, в которой находится исполняемый файл / скрипт."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.realpath(__file__))


def ensure_saves_file(file_path: str) -> None:
    """Создаёт файл сохранения, если его ещё нет."""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("[]")


def validate_task_index(index_str: str, task_list: list) -> bool:
    """Проверяет, что введённый номер задачи корректен."""
    if not index_str.isdigit():
        return False
    index = int(index_str)
    return 1 <= index <= len(task_list)