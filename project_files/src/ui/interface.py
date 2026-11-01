"""
Слой интерфейса (Interface).
Собирает GUI из кастомных компонентов.
Версия: 0.2.0
"""

import tkinter as tk
from tkinter import messagebox, simpledialog

from .AppFrame import AppFrame
from .AppButton import AppButton
from .AppLabel import AppLabel
from .AppListbox import AppListbox

import sys
import os

# Добавляем путь к src, чтобы импортировать config и core
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    COLOR_BG_DARK,
    COLOR_BG_FRAME,
    COLOR_ACCENT,
)
from core import add_task, edit_task, delete_task, get_task_display_text
from storage import load_tasks, save_tasks
from config import NAME_FILE_SAVES
from utils import ensure_saves_file


class Interface:
    """Главный класс интерфейса приложения Task Manager."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Task Manager — Develop-App Course")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=COLOR_BG_DARK)
        self.root.resizable(False, False)

        # Данные
        ensure_saves_file(NAME_FILE_SAVES)
        self.tasks = load_tasks(NAME_FILE_SAVES)

        # Фреймы
        self.frames = {}
        self.listbox = None

        self._create_interface()
        self._show_frame("menu")

    def _create_interface(self):
        """Создаёт все фреймы и элементы управления."""
        self._create_menu_frame()
        self._create_tasks_frame()
        self._create_add_frame()

    def _create_menu_frame(self):
        """Главное меню."""
        frame = AppFrame(self.root, bg=COLOR_BG_FRAME, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.frames["menu"] = frame

        AppLabel(frame, text="Task Manager", font_size=18, bold=True, bg=COLOR_BG_FRAME)
        AppLabel(frame, text="Слоистая архитектура • Урок 13–14", font_size=10, bg=COLOR_BG_FRAME)

        AppButton(frame, text="📋 Посмотреть все задачи", command=self._open_tasks)
        AppButton(frame, text="➕ Добавить задачу", command=self._open_add)
        AppButton(frame, text="💾 Сохранить и выйти", command=self._save_and_exit, bg="#c0392b")

    def _create_tasks_frame(self):
        """Фрейм со списком задач."""
        frame = AppFrame(self.root, bg=COLOR_BG_FRAME, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.frames["tasks"] = frame

        AppLabel(frame, text="Список задач", font_size=16, bold=True, bg=COLOR_BG_FRAME)

        self.listbox = AppListbox(frame)

        btn_frame = tk.Frame(frame, bg=COLOR_BG_FRAME)
        btn_frame.pack(pady=5)

        AppButton(btn_frame, text="✏️ Редактировать", width=16, command=self._edit_selected)
        AppButton(btn_frame, text="🗑️ Удалить", width=16, command=self._delete_selected, bg="#c0392b")
        AppButton(btn_frame, text="⬅ Назад в меню", width=16, command=lambda: self._show_frame("menu"))

    def _create_add_frame(self):
        """Фрейм добавления задачи."""
        frame = AppFrame(self.root, bg=COLOR_BG_FRAME, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.frames["add"] = frame

        AppLabel(frame, text="Новая задача", font_size=16, bold=True, bg=COLOR_BG_FRAME)

        AppLabel(frame, text="Название:", font_size=11, bg=COLOR_BG_FRAME)
        self.entry_name = tk.Entry(
            frame,
            width=45,
            font=("Segoe UI", 11),
            bg="#1e1e2e",
            fg="#e0e0e0",
            insertbackground="#e0e0e0",
            relief=tk.FLAT,
        )
        self.entry_name.pack(pady=5, padx=20)

        AppLabel(frame, text="Содержимое:", font_size=11, bg=COLOR_BG_FRAME)
        self.entry_content = tk.Entry(
            frame,
            width=45,
            font=("Segoe UI", 11),
            bg="#1e1e2e",
            fg="#e0e0e0",
            insertbackground="#e0e0e0",
            relief=tk.FLAT,
        )
        self.entry_content.pack(pady=5, padx=20)

        AppButton(frame, text="✅ Сохранить задачу", command=self._save_new_task)
        AppButton(frame, text="⬅ Назад", command=lambda: self._show_frame("menu"), bg="#555")

    def _show_frame(self, name: str):
        """Показывает нужный фрейм, скрывая остальные."""
        for f in self.frames.values():
            f.hide()
        self.frames[name].show()

        if name == "tasks":
            self._refresh_task_list()

    def _open_tasks(self):
        self._show_frame("tasks")

    def _open_add(self):
        self.entry_name.delete(0, tk.END)
        self.entry_content.delete(0, tk.END)
        self._show_frame("add")

    def _refresh_task_list(self):
        """Обновляет отображение задач через AppListbox."""
        items = [
            get_task_display_text(task, i + 1)
            for i, task in enumerate(self.tasks)
        ]
        self.listbox.fill(items)

    def _save_new_task(self):
        name = self.entry_name.get()
        content = self.entry_content.get()

        task = add_task(self.tasks, name, content)
        if task is None:
            messagebox.showwarning("Ошибка", "Название и содержимое не могут быть пустыми!")
            return

        save_tasks(self.tasks, NAME_FILE_SAVES)
        messagebox.showinfo("Успех", f"Задача «{task['name']}» добавлена!")
        self._show_frame("menu")

    def _edit_selected(self):
        index = self.listbox.get_selected_index()
        if index is None:
            messagebox.showwarning("Внимание", "Выберите задачу для редактирования.")
            return

        task = self.tasks[index]
        new_name = simpledialog.askstring(
            "Редактирование",
            "Новое название:",
            initialvalue=task["name"],
            parent=self.root,
        )
        if new_name is None:
            return

        new_content = simpledialog.askstring(
            "Редактирование",
            "Новое содержимое:",
            initialvalue=task["content"],
            parent=self.root,
        )
        if new_content is None:
            return

        if edit_task(self.tasks, index, new_name, new_content):
            save_tasks(self.tasks, NAME_FILE_SAVES)
            self._refresh_task_list()
            messagebox.showinfo("Успех", "Задача обновлена!")
        else:
            messagebox.showwarning("Ошибка", "Название и содержимое не могут быть пустыми!")

    def _delete_selected(self):
        index = self.listbox.get_selected_index()
        if index is None:
            messagebox.showwarning("Внимание", "Выберите задачу для удаления.")
            return

        task_name = self.tasks[index]["name"]
        if messagebox.askyesno("Подтверждение", f"Удалить задачу «{task_name}»?"):
            if delete_task(self.tasks, index):
                save_tasks(self.tasks, NAME_FILE_SAVES)
                self._refresh_task_list()
                messagebox.showinfo("Успех", "Задача удалена!")

    def _save_and_exit(self):
        save_tasks(self.tasks, NAME_FILE_SAVES)
        self.root.destroy()

    def run(self):
        """Запускает главный цикл приложения."""
        self.root.mainloop()