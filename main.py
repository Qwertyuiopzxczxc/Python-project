"""Основной файл приложения

    версия 0.0.5

    === Описание ===
        Приложение может сохранять задачи, выдаёт список задач,
        может удалять и редактировать задачи.
"""

import processes

collection = ['task1', 'task2']  # список задач
is_running = True


def show_collection():
    print("=" * 45)
    for i, task in enumerate(collection):
        print(i + 1, task)
    print("=" * 45)


def show_menu():
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Редактировать задачу")
    print("4 - Удалить задачу")
    print("5 - Выход")

def check_confirm(select_task, task_list):
    if (select_task.isdigit()):
        if(select_task > 0 and select_task <= len(task_list)):
            return 1
        else:
            return 2
    else:
        return 3

def delete_task(task_collection):
    delete_tasks = input("Введите номер задачи для управления")
    if check_confirm(delete_tasks, task_collection):
        task_collection.pop(int(delete_tasks)-1)
        print(f"Задача с номером {delete_tasks} успешно удалена")
    elif check_confirm(delete_tasks, task_collection) == 2:
        print(f"Задачи с номером {delete_tasks} нет в списке")
    elif check_confirm(delete_tasks, task_collection) == 3:
        print(f"Введите именно номер задачи!")

def edit_task(task_collection):
    selected_task = input("Введите номер задачи")
    if check_confirm(selected_task, task_collection) == 2 :
        new_task = input("новое имя задачи")
        task_collection[int(new_task)-1] = new_task


while is_running:
    show_menu()
    choice_user = input("Введите ваш выбор: ")

    match choice_user:
        case "1":
            show_collection()
            processes.show_message("Список задач показан")

        case "2":
            new_task = input("Введите имя задачи для добавления: ")
            if len(new_task) < 2 :
                print("название не может быть пустым!")
                continue
            else:
                collection.append(new_task)
            collection.append(new_task)
            processes.show_message("Задача добавлена")

        case "3":
            show_collection()
            select = int(input("Введите номер задачи: "))
            new_name = input("Введите новое имя задачи: ")
            collection[select - 1] = new_name
            processes.show_message("Задача изменена")

        case "4":
            show_collection()
            delete = int(input("Введите номер задачи для удаления: "))
            collection.pop(delete - 1)
            processes.show_message("Задача удалена")

        case "5":
            is_running = False
            processes.show_message("До свидания!")

        case _:
            processes.show_message("Такого пункта нет...")
