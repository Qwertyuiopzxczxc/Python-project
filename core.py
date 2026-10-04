# ==================================================
#        Модуль с основными механиками
# ==================================================

from utils import check_confirm


def add_task(task_collection: list) -> None:
    """Добавляет новую задачу в коллекцию."""
    task_name = input("Введите имя задачи: ").strip()
    task_content = input("Введите содержимое задачи: ").strip()

    if not task_name:
        print("Имя задачи не может быть пустым!")
        return

    if not task_content:
        print("Содержимое задачи не может быть пустым!")
        return

    full_task = f"{task_name} | {task_content}"
    task_collection.append(full_task)
    print(f"Задача «{task_name}» успешно добавлена!")


def edit_task(task_collection: list) -> None:
    """Редактирует существующую задачу."""
    edit_task_number = input("Введите номер задачи: ").strip()

    if not check_confirm(edit_task_number, task_collection):
        return

    edit_name = input("Новое имя задачи: ").strip()
    edit_content = input("Новое содержимое задачи: ").strip()

    if not edit_name:
        print("Название задачи не может быть пустым!")
        return

    if not edit_content:
        print("Содержимое задачи не может быть пустым!")
        return

    index = int(edit_task_number) - 1
    task_collection[index] = f"{edit_name} | {edit_content}"
    print(f"Задача «{edit_name}» успешно изменена!")


def delete_tasks(task_collection: list) -> None:
    """Удаляет задачу по номеру."""
    delete_task = input("Введите номер задачи: ").strip()

    if not check_confirm(delete_task, task_collection):
        return

    index = int(delete_task) - 1
    removed = task_collection.pop(index)
    name = removed.split("|", 1)[0].strip()
    print(f"Задача «{name}» удалена!")
