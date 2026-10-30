"""
                              === Функции для просмотра и показа задач ===

                                    === Версия приложения: 0.0.9 ===
"""

### Показ списка задач
import tkinter as tk

from python.TM.src.ui.interface import Interface
from storage import  load_tasks, save_tasks
from config import NAME_FILE_SAVES
collections = load_tasks([],NAME_FILE_SAVES)
ui = Interface()

def main():
    show_all_tasks()

def show_all_tasks():
        for number, content in enumerate(collection):
            print(number, content)
            ui.list_task.add_to_list(content["name"])

def show_details():
    pass

main()
create_menu()
root.mainloop()
