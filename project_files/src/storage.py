"""
Слой хранения данных (Storage).
Загрузка и сохранение задач в JSON.
Версия: 0.2.0
"""

import json
from typing import List, Dict, Any


def load_tasks(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список задач из JSON-файла.
    Возвращает пустой список, если файл не найден или повреждён.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks: List[Dict[str, Any]], file_path: str) -> bool:
    """
    Сохраняет список задач в JSON-файл.
    Возвращает True при успехе, False при ошибке.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
        return True
    except OSError:
        return False