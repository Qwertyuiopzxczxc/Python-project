""" =========================================================
    Interface — прослойка между логикой и tkinter.
    Не знает про задачи. Только создаёт и обновляет виджеты.
    =========================================================
"""
import tkinter as tk
from tkinter import messagebox
from components import AppLabel, AppEntry, AppButton, AppListbox, AppFrame


class Interface:
    """Фасад над tkinter: единый API для TaskManager."""

    def __init__(self, root: tk.Tk | None = None, title: str = "Task Manager v0.2.0", width: int = 560, height: int = 540) -> None:
        """Создать корневое окно, настроить размеры и стиль."""
        if isinstance(root, str):
            title = root
            root = None

        self.root = root if root is not None else tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.configure(bg="#141518")

        self.title_entry: AppEntry | None = None
        self.desc_entry: AppEntry | None = None
        self.author_entry: AppEntry | None = None
        self.listbox: AppListbox | None = None

    # ---------- жизненный цикл ----------
    def run(self) -> None:
        """Запустить главный цикл."""
        self.root.mainloop()

    def quit(self) -> None:
        """Закрыть окно."""
        self.root.destroy()

    def clear(self) -> None:
        """Удалить все дочерние виджеты."""
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------- построение ----------
    def build(self, on_create=None, on_edit=None, on_delete=None, on_toggle=None, on_refresh=None) -> None:
        """Собрать базовый каркас: заголовок, список, поле ввода, кнопки."""
        self.clear()

        header = AppLabel(self.root, text="Менеджер задач v0.2.0", font=("Segoe UI", 14, "bold"))
        header.pack(pady=(14, 8))

        # Блок полей ввода
        form_frame = AppFrame(self.root)
        form_frame.pack(fill="x", padx=16, pady=4)

        AppLabel(form_frame, text="Название *:", fg="#9ca3af").grid(row=0, column=0, sticky="w", pady=3)
        self.title_entry = AppEntry(form_frame)
        self.title_entry.grid(row=0, column=1, sticky="we", padx=(8, 0), pady=3, ipady=3)

        AppLabel(form_frame, text="Описание:", fg="#9ca3af").grid(row=1, column=0, sticky="w", pady=3)
        self.desc_entry = AppEntry(form_frame)
        self.desc_entry.grid(row=1, column=1, sticky="we", padx=(8, 0), pady=3, ipady=3)

        AppLabel(form_frame, text="Автор:", fg="#9ca3af").grid(row=2, column=0, sticky="w", pady=3)
        self.author_entry = AppEntry(form_frame)
        self.author_entry.grid(row=2, column=1, sticky="we", padx=(8, 0), pady=3, ipady=3)

        form_frame.columnconfigure(1, weight=1)

        # Список задач
        list_frame = AppFrame(self.root)
        list_frame.pack(fill="both", expand=True, padx=16, pady=8)

        self.listbox = AppListbox(list_frame, height=12)
        self.listbox.pack(fill="both", expand=True)
        self.listbox.bind("<<ListboxSelect>>", self._on_select_fill_inputs)
        if on_toggle:
            self.listbox.bind("<Double-Button-1>", lambda e: on_toggle())

        # Верхний ряд кнопок (CRUD)
        btn_row1 = AppFrame(self.root)
        btn_row1.pack(fill="x", padx=16, pady=(2, 4))

        AppButton(btn_row1, text="+ Создать", bg="#4f46e5", command=on_create).pack(side="left", expand=True, fill="x", padx=(0, 4))
        AppButton(btn_row1, text="✎ Изменить", command=on_edit).pack(side="left", expand=True, fill="x", padx=4)
        AppButton(btn_row1, text="✓ Статус", command=on_toggle).pack(side="left", expand=True, fill="x", padx=4)
        AppButton(btn_row1, text="✕ Удалить", bg="#3a1d22", command=on_delete).pack(side="left", expand=True, fill="x", padx=(4, 0))

        # Нижний ряд кнопок (служебные)
        btn_row2 = AppFrame(self.root)
        btn_row2.pack(fill="x", padx=16, pady=(2, 14))

        AppButton(btn_row2, text="Очистить поля", command=self.clear_input).pack(side="left", expand=True, fill="x", padx=(0, 4))
        if on_refresh:
            AppButton(btn_row2, text="Обновить", command=on_refresh).pack(side="left", expand=True, fill="x", padx=4)
        AppButton(btn_row2, text="Выход", command=self.quit).pack(side="left", expand=True, fill="x", padx=(4, 0))

    # ---------- ввод ----------
    def get_input(self) -> dict:
        """Вернуть {title, description, author} из полей ввода."""
        return {
            "title": self.title_entry.get().strip() if self.title_entry else "",
            "description": self.desc_entry.get().strip() if self.desc_entry else "",
            "author": (self.author_entry.get().strip() or "—") if self.author_entry else "—",
        }

    def clear_input(self) -> None:
        """Очистить поля ввода."""
        for entry in (self.title_entry, self.desc_entry, self.author_entry):
            if entry is not None:
                entry.delete(0, tk.END)

    def set_input(self, title: str = "", description: str = "", author: str = "") -> None:
        """Заполнить поля ввода данными выбранной задачи для удобного редактирования."""
        self.clear_input()
        if self.title_entry:
            self.title_entry.insert(0, title)
        if self.desc_entry:
            self.desc_entry.insert(0, description)
        if self.author_entry and author != "—":
            self.author_entry.insert(0, author)

    # ---------- отображение ----------
    def show_tasks(self, tasks: list) -> None:
        """Заполнить список задач (list[Task] или list[dict])."""
        if self.listbox is None:
            return
        self._cached_tasks = tasks
        self.listbox.delete(0, tk.END)

        for item in tasks:
            if isinstance(item, dict):
                t_id = item.get("id", "?")
                title = item.get("title", "")
                desc = item.get("description", "")
                status = item.get("status", False)
                author = item.get("author", "—")
            else:
                t_id = item.id if item.id is not None else "?"
                title = item.title
                desc = item.description
                status = item.status
                author = item.author

            mark = "[✓]" if status else "[ ]"
            desc_str = f" — {desc}" if desc else ""
            author_str = f" ({author})" if author and author != "—" else ""
            self.listbox.insert(tk.END, f"{mark} #{t_id} {title}{desc_str}{author_str}")

    def _on_select_fill_inputs(self, event=None) -> None:
        """При выборе строки в списке подставляет её текст в поля ввода."""
        idx = self.get_selected_index()
        if idx is None or not hasattr(self, "_cached_tasks"):
            return
        if 0 <= idx < len(self._cached_tasks):
            item = self._cached_tasks[idx]
            if isinstance(item, dict):
                self.set_input(item.get("title", ""), item.get("description", ""), item.get("author", ""))
            else:
                self.set_input(item.title, item.description, item.author)

    def show_message(self, title: str, text: str) -> None:
        """Показать информационное сообщение."""
        messagebox.showinfo(title, text, parent=self.root)

    def show_warning(self, title: str, text: str) -> None:
        """Показать предупреждение."""
        messagebox.showwarning(title, text, parent=self.root)

    def ask_confirm(self, title: str, text: str) -> bool:
        """Спросить подтверждение. True — да, False — нет."""
        return messagebox.askyesno(title, text, parent=self.root)

    def get_selected_index(self) -> int | None:
        """Индекс выбранной строки в списке или None."""
        if self.listbox is None:
            return None
        selection = self.listbox.curselection()
        return selection[0] if selection else None
