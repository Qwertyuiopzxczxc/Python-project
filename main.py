"""Основной файл приложения Task Manager

версия 0.0.7

=== Описание ===
    Приложение может сохранять задачи, выдаёт список задач,
    может удалять и редактировать задачи.
    Задачи сохраняются в файл tasks.txt.
"""

import processes
import os

FILENAME = "tasks.txt"


def load_tasks():
    """Загружает задачи из файла"""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file if line.strip()]
    return tasks


def save_tasks(task_collection):
    """Сохраняет задачи в файл"""
    with open(FILENAME, "w", encoding="utf-8") as file:
        for task in task_collection:
            file.write(task + "\n")


def show_collection(task_collection):
    """Красивый вывод списка задач"""
    print("=" * 45)
    if not task_collection:
        print("Список задач пуст")
    else:
        for i, task in enumerate(task_collection, start=1):
            print(f"{i}. {task}")
    print("=" * 45)


def show_menu():
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Редактировать задачу")
    print("4 - Удалить задачу")
    print("5 - Выход")


def edited_task(task_collection):
    """Редактирует задачу (вызывается в case 3)"""
    if not task_collection:
        print("Список задач пуст. Нечего редактировать.")
        return

    show_collection(task_collection)
    try:
        select = int(input("Введите номер задачи для редактирования: "))
        if 1 <= select <= len(task_collection):
            new_name = input("Введите новое имя задачи: ").strip()
            if len(new_name) < 2:
                print("Название не может быть слишком коротким!")
                return
            task_collection[select - 1] = new_name
            save_tasks(task_collection)
            processes.show_message("Задача изменена")
        else:
            print("Задачи с таким номером нет!")
    except ValueError:
        print("Введите именно номер задачи!")


def deleted_task(task_collection):
    """Удаляет задачу (вызывается в case 4)"""
    if not task_collection:
        print("Список задач пуст. Нечего удалять.")
        return

    show_collection(task_collection)
    try:
        select = int(input("Введите номер задачи для удаления: "))
        if 1 <= select <= len(task_collection):
            deleted = task_collection.pop(select - 1)
            save_tasks(task_collection)
            processes.show_message(f"Задача «{deleted}» удалена")
        else:
            print("Задачи с таким номером нет!")
    except ValueError:
        print("Введите именно номер задачи!")


def main():
    """Главная функция с циклом while"""
    collection = load_tasks()   # загружаем задачи при старте
    is_running = True

    while is_running:
        show_menu()
        choice_user = input("Введите ваш выбор: ").strip()

        match choice_user:
            case "1":
                show_collection(collection)
                processes.show_message("Список задач показан")

            case "2":
                new_task = input("Введите имя задачи для добавления: ").strip()
                if len(new_task) < 2:
                    print("Название не может быть пустым или слишком коротким!")
                    continue
                collection.append(new_task)
                save_tasks(collection)
                processes.show_message("Задача добавлена")

            case "3":
                edited_task(collection)   # вызов функции вне цикла

            case "4":
                deleted_task(collection)  # вызов функции вне цикла

            case "5":
                is_running = False
                processes.show_message("До свидания!")

            case _:
                processes.show_message("Такого пункта нет...")


# Вызов главной функции в конце скрипта
if __name__ == "__main__":
    main()
