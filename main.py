"""Основной файл приложения

    версия 0.0.7

    === Описание ===
        Приложение может сохранять задачи, выдает список задач, и может удалять и редактировать задачи

"""
from random import choice
import processes
import os

collection = []  # list of tasks
is_running = True
name_files = "save.txt"


def show_collection(task_collection):
    print("=" * 45)
    for i, j in enumerate(collection):
        print(i + 1, j)
    print("=" * 45)


def show_menu():
    print("1 - Показать задачи \n"
          "2 - Добавить задачу \n"
          "3 - Редактировать задачи \n"
          "4 - Удаление задачи \n"
          "5 - Выход")


def check_confirm(select_task, task_list):
    if select_task.isdigit():
        if int(select_task) > 0 and int(select_task) <= len(task_list):
            return True
        else:
            print(f"Задачи с номером {select_task} нет в списке!")
            return False
    else:
        print(f"Введите именно номер задачи!")
        return False

def delete_tasks(task_collection):
    delete_task = input("Введите номер задачи: ")
    if check_confirm(delete_task, task_collection) == 1:
        task_collection.pop(int(delete_task) - 1)
        print(f"Задача {delete_task} удалена!")
    else:
        print("Неверный номер задачи!")


def edit_task(task_collection):
    edit_task = input("Введите номер задачи: ")
    if check_confirm(edit_task, task_collection) == 1:
        task_collection[int(edit_task) - 1] = input("Новое имя задачи: ")
    else:
        print("Неверный номер задачи!")


def add_task(task_collection):
    task_name = input("Введите имя задачи для добавления: ")
    task_content = input("Введите сожержанте задачи")
    if task_name.startswith(' ') or task_content.endswith(' '):
        if len(task_content) < 2:
            print("Имя задачи и сожержание не должно быть пустым!")
            return


def load_file(tsak_list, file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            tsak_list.append(line)

def save_file(task_list, file_name):
    with open(name_files, "w", encoding="utf-8") as file:
        for task in task_list:
            file.writelines(f"{task}\n")
    pass

def main():
    global is_running
    global name_files
    while is_running:
        show_menu()
        choice_user = input('Введите ваш выбор: ')
        task_collection = []


        match choice_user:
            case "1":
                show_collection(task_collection)
                load_file(task_collection, name_files)
            case "2":
                add_task(task_collection)
                save_file(task_collection, name_files)

            case "3":
                show_collection(collection)
                edit_task(collection)

            case "4":
                show_collection(collection)
                delete_tasks(collection)

            case "0":
                is_running = False
                print("До свидиния!")

            case _:
                print('Такого пункта нет...')


if __name__ == "__main__":
    main()
