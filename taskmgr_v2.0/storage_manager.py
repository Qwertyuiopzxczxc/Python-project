""" =========================================================
    StorageManager — сохранение и загрузка задач.
    Сейчас JSON, в будущем — замена на БД без смены API.
    =========================================================
"""
import json
import os
from task import Task


class StorageManager:
    """Управляет персистентностью коллекции задач."""

    def __init__(self, path: str = "tasks.json") -> None:
        """Запомнить путь к файлу, при необходимости — создать."""
        self.path = path
        if not os.path.exists(self.path):
            self.save([])

    def load(self) -> list[Task]:
        """Прочитать все задачи из хранилища."""
        if not os.path.exists(self.path):
            return []
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                data = json.load(file)
                if not isinstance(data, list):
                    return []
                return [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, OSError):
            return []

    def save(self, tasks: list[Task]) -> None:
        """Записать весь список задач в хранилище."""
        with open(self.path, "w", encoding="utf-8") as file:
            data = [task.to_dict() for task in tasks]
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add(self, task: Task) -> None:
        """Добавить одну задачу."""
        tasks = self.load()
        if task.id is None:
            max_id = max((t.id for t in tasks if t.id is not None), default=0)
            task.id = max_id + 1
        tasks.append(task)
        self.save(tasks)

    def update(self, task_id: int, task: Task) -> None:
        """Обновить задачу по id."""
        tasks = self.load()
        for index, current in enumerate(tasks):
            if current.id == task_id:
                task.id = task_id
                tasks[index] = task
                break
        self.save(tasks)

    def delete(self, task_id: int) -> None:
        """Удалить задачу по id."""
        tasks = self.load()
        tasks = [t for t in tasks if t.id != task_id]
        self.save(tasks)
