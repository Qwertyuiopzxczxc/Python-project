"""
Кастомный класс списка (AppListbox).
Используется для отображения задач.
Версия: 0.2.0
"""

import tkinter as tk
from tkinter import font as tkfont


class AppListbox(tk.Listbox):
    """Список задач с единым стилем приложения."""

    def __init__(
        self,
        master,
        width: int = 55,
        height: int = 15,
        bg: str = "#1e1e2e",
        fg: str = "#e0e0e0",
        selectbackground: str = "#4a6cf7",
        selectforeground: str = "#ffffff",
        **kwargs
    ):
        super().__init__(
            master,
            width=width,
            height=height,
            bg=bg,
            fg=fg,
            selectbackground=selectbackground,
            selectforeground=selectforeground,
            relief=tk.FLAT,
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#3b5bdb",
            font=tkfont.Font(family="Consolas", size=10),
            activestyle="none",
            **kwargs
        )
        self.pack(pady=10, padx=15, fill=tk.BOTH, expand=True)

    def clear(self) -> None:
        """Очищает весь список."""
        self.delete(0, tk.END)

    def add_item(self, text: str) -> None:
        """Добавляет элемент в конец списка."""
        self.insert(tk.END, text)

    def fill(self, items: list) -> None:
        """Заполняет список переданными элементами (предварительно очищает)."""
        self.clear()
        for item in items:
            self.add_item(item)

    def get_selected_index(self):
        """Возвращает индекс выбранного элемента или None."""
        selection = self.curselection()
        if selection:
            return selection[0]
        return None