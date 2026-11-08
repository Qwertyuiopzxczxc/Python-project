""" =========================================================
    Точка входа приложения.
    =========================================================
"""
import tkinter as tk
from task_manager import TaskManager


def main() -> None:
    """Создать окно, собрать TaskManager, запустить."""
    root = tk.Tk()
    app = TaskManager(root)
    app.run()


if __name__ == "__main__":
    main()
