"""
                    === Основной файл приложения ===

                          === Версия 0.0.9 ===
"""

from storege import load_tasks, save_tasks
from view import show_menu, show_collection
from core import add_task, edit_task, delete_tasks
from config import NAME_FILE_SAVES

collection = []


def main():
    name_file = NAME_FILE_SAVES

    collection.extend(load_tasks(name_file))

    is_running = True

    while is_running:
        show_menu()
        choice_user = input("Введите ваш выбор: ")

        match choice_user:

            case "1":
                show_collection(collection)

            case "2":
                add_task(collection)
                save_tasks(collection, name_file)

            case "3":
                show_collection(collection)
                edit_task(collection)
                save_tasks(collection, name_file)

            case "4":
                show_collection(collection)
                delete_tasks(collection)
                save_tasks(collection, name_file)

            case "5":
                save_tasks(collection, name_file)
                is_running = False
                print("До свидания!")

            case _:
                print("Такого пункта нет...")

if __name__ == "__main__":
    main()