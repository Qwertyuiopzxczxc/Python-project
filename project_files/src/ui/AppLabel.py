"""
Кастомный класс метки (AppLabel).
Используется для заголовков и текстовых элементов интерфейса.
Версия: 0.2.0
"""

import tkinter as tk
from tkinter import font as tkfont


class AppLabel(tk.Label):
    """Метка с единым стилем приложения."""

    def __init__(
        self,
        master,
        text: str = "",
        font_size: int = 12,
        bold: bool = False,
        fg: str = "#e0e0e0",
        bg: str = "#2a2a3d",
        **kwargs
    ):
        weight = "bold" if bold else "normal"
        super().__init__(
            master,
            text=text,
            fg=fg,
            bg=bg,
            font=tkfont.Font(family="Segoe UI", size=font_size, weight=weight),
            **kwargs
        )
        self.pack(pady=8, padx=10)