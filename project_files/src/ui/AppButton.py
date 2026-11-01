"""
Кастомный класс кнопки (AppButton).
Версия: 0.2.0
"""

import tkinter as tk
from tkinter import font as tkfont


class AppButton(tk.Button):
    """Кнопка с единым стилем приложения."""

    def __init__(
        self,
        master,
        text: str = "",
        command=None,
        width: int = 22,
        height: int = 2,
        bg: str = "#3b5bdb",
        fg: str = "#ffffff",
        activebackground: str = "#5c7cfa",
        activeforeground: str = "#ffffff",
        **kwargs
    ):
        super().__init__(
            master,
            text=text,
            command=command,
            width=width,
            height=height,
            bg=bg,
            fg=fg,
            activebackground=activebackground,
            activeforeground=activeforeground,
            relief=tk.FLAT,
            cursor="hand2",
            font=tkfont.Font(family="Segoe UI", size=10, weight="bold"),
            **kwargs
        )
        self.pack(pady=6, padx=10)