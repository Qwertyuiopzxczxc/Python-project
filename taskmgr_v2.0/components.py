""" =========================================================
    Компоненты UI. Наследники tk-виджетов с единым стилем.
    Interface использует ТОЛЬКО эти классы.
    =========================================================
"""
import tkinter as tk


class AppLabel(tk.Label):
    def __init__(self, master, text: str = "", **kwargs) -> None:
        style = {
            "bg": "#141518",
            "fg": "#f3f4f6",
            "font": ("Segoe UI", 10),
        }
        style.update(kwargs)
        super().__init__(master, text=text, **style)


class AppEntry(tk.Entry):
    def __init__(self, master, **kwargs) -> None:
        style = {
            "bg": "#1b1d21",
            "fg": "#f3f4f6",
            "insertbackground": "#f3f4f6",
            "relief": "flat",
            "font": ("Segoe UI", 10),
            "highlightthickness": 1,
            "highlightbackground": "#2a2e34",
            "highlightcolor": "#4f46e5",
        }
        style.update(kwargs)
        super().__init__(master, **style)


class AppButton(tk.Button):
    def __init__(self, master, text: str, command=None, **kwargs) -> None:
        style = {
            "bg": "#22252a",
            "fg": "#f3f4f6",
            "activebackground": "#4f46e5",
            "activeforeground": "#ffffff",
            "relief": "flat",
            "padx": 10,
            "pady": 6,
            "font": ("Segoe UI", 9, "bold"),
            "cursor": "hand2",
        }
        style.update(kwargs)
        super().__init__(master, text=text, command=command, **style)


class AppListbox(tk.Listbox):
    def __init__(self, master, **kwargs) -> None:
        style = {
            "bg": "#1b1d21",
            "fg": "#f3f4f6",
            "selectbackground": "#4f46e5",
            "selectforeground": "#ffffff",
            "relief": "flat",
            "font": ("Consolas", 10),
            "highlightthickness": 1,
            "highlightbackground": "#2a2e34",
            "highlightcolor": "#4f46e5",
            "activestyle": "none",
        }
        style.update(kwargs)
        super().__init__(master, **style)


class AppFrame(tk.Frame):
    def __init__(self, master, **kwargs) -> None:
        style = {
            "bg": "#141518",
        }
        style.update(kwargs)
        super().__init__(master, **style)
