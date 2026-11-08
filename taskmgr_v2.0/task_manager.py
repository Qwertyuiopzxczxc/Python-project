""" =========================================================
    TaskManager — главный фасад.
    Связывает Task, StorageManager и Interface.
    =========================================================
"""
import tkinter as tk
from task import Task
from storage_manager import StorageManager
from interface import Interface


class TaskManager:
    """Оркестратор приложения. Единственная точка входа для UI."""

    def __init__(self, root: tk.Tk | None = None, storage_path: str = "tasks.json") -> None:
        """Создать StorageManager и Interface, привязать колбэки."""
        self.storage = StorageManager(storage_path)
        self.ui = Interface(root=root)
        self.tasks: list[Task] = []

        self.ui.build(
            on_create=self.create_task,
            on_edit=self.edit_task,
            on_delete=self.delete_task,
            on_toggle=self.toggle_status,
            on_refresh=self.refresh,
        )
        self.refresh()

    # ---------- CRUD ----------
    def create_task(self) -> None:
        """Прочитать ввод → создать Task → сохранить → обновить список."""
        data = self.ui.get_input()
        if not data["title"]:
            self.ui.show_warning("Внимание", "Введите название задачи!")
            return

        new_task = Task(
            title=data["title"],
            description=data["description"],
            author=data["author"],
        )
        self.storage.add(new_task)
        self.ui.clear_input()
        self.refresh()

    def edit_task(self) -> None:
        """Взять выбранную задачу → изменить → сохранить → обновить."""
        index = self.ui.get_selected_index()
        if index is None or index >= len(self.tasks):
            self.ui.show_warning("Внимание", "Выберите задачу из списка для изменения!")
            return

        data = self.ui.get_input()
        if not data["title"]:
            self.ui.show_warning("Внимание", "Название задачи не может быть пустым!")
            return

        selected_task = self.tasks[index]
        selected_task.title = data["title"]
        selected_task.description = data["description"]
        selected_task.author = data["author"]

        self.storage.update(selected_task.id, selected_task)
        self.ui.clear_input()
        self.refresh()

    def delete_task(self) -> None:
        """Удалить выбранную задачу (с подтверждением)."""
        index = self.ui.get_selected_index()
        if index is None or index >= len(self.tasks):
            self.ui.show_warning("Внимание", "Выберите задачу для удаления!")
            return

        selected_task = self.tasks[index]
        if self.ui.ask_confirm("Удаление", f"Удалить задачу «{selected_task.title}»?"):
            self.storage.delete(selected_task.id)
            self.ui.clear_input()
            self.refresh()

    def toggle_status(self) -> None:
        """Переключить статус выбранной задачи."""
        index = self.ui.get_selected_index()
        if index is None or index >= len(self.tasks):
            self.ui.show_warning("Внимание", "Выберите задачу для смены статуса!")
            return

        selected_task = self.tasks[index]
        selected_task.status = not selected_task.status
        self.storage.update(selected_task.id, selected_task)
        self.refresh()

    toggle_done = toggle_status

    # ---------- служебное ----------
    def refresh(self) -> None:
        """Перечитать задачи из StorageManager и отрисовать."""
        self.tasks = self.storage.load()
        self.ui.show_tasks(self.tasks)

    def run(self) -> None:
        """Передать управление Interface."""
        self.ui.run()
