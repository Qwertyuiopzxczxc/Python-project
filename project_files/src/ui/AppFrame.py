"""
Кастомный класс фрейма (AppFrame).
Версия: 0.2.0
"""

import tkinter as tk


class AppFrame(tk.Frame):
    """Фрейм с возможностью скрытия/показа."""

    def __init__(
        self,
        master,
        bg: str = "#2a2a3d",
        width: int = 500,
        height: int = 450,
        **kwargs
    ):
        super().__init__(
            master,
            bg=bg,
            width=width,
            height=height,
            **kwargs
        )
        self.pack_propagate(False)

    def show(self) -> None:
        """Показывает фрейм."""
        self.pack(fill=tk.BOTH, expand=True)

    def hide(self) -> None:
        """Скрывает фрейм."""
        self.pack_forget()