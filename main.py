"""## Версия 0.0.5

    Точка входа в приложение Task Manager
    --- description ---
    Изменения:
    - добавлена функция show_message (сообщения о результатах добавления, редактирования, удаления)
    - доработана функция show_collection (принимает список и форматированно выводит его)
    - исправлены ошибки с индексами и проверками ввода
"""

collection = ['1','2'] #list

task_number = 0

is_running = True #flag

def show_message(action, success, detail=""):
    if success:
        print(f"Успешно: {action} {detail}".strip())
    else:
        print(f"Ошибка: {action} {detail}".strip())

def listcheck(task_collection, name):
    if name in task_collection:
        show_message("добавление", False, f"— задача «{name}» уже существует")
        return True
    else:
        return False

def show_collection(task_collection):
    print('=' * 30)
    if not task_collection:
        print("Список задач пуст.")
    else:
        for task_number, j in enumerate(task_collection, start=1):
            print(f"{task_number}. {j}")
    print('=' * 30)

while is_running:

    print("1 - показать задачи | 2 - добавить задачу | 3 - редактировать задачу | 4 - удалить задачу | 0 - выход")

    choice_user = input('Введите ваш выбор ( 0 | 1 | 2 | 3 | 4 )')

    if choice_user == '0':
        print("Программа завершена.")
        is_running = False
        continue

    if choice_user == '1' or choice_user == '2' or choice_user == '3' or choice_user == '4':
        match int(choice_user):

            case 1:
                show_collection(collection)
            case 2:
                task_name = input('Название задачи (или оставьте пустым): ')
                match (task_name):
                    case "":
                        task_name = 'task'
                        task_number += 1
                        collection.append(f"{task_name} {task_number}")
                        show_message("добавление", True, f"— создана задача «{task_name} {task_number}»")
                    case _:
                        if not listcheck(collection, task_name):
                            collection.append(f"{task_name}")
                            show_message("добавление", True, f"— добавлена задача «{task_name}»")
            case 3:
                show_collection(collection)
                select_edit = input('введите номер задачи')
                if select_edit.isdigit():
                    if int(select_edit) > 0 and int(select_edit) <= len(collection):
                        edit_name = input('новое имя задачи')
                        old_name = collection[int(select_edit) - 1]
                        collection[int(select_edit) - 1] = edit_name
                        show_message("редактирование", True, f"— «{old_name}» → «{edit_name}»")
                    else:
                        show_message("редактирование", False, "— задачи с таким номером нет в списке")
                else:
                    show_message("редактирование", False, "— введите номер задачи")


            case 4:
                show_collection(collection)
                delete_edit = input('введите номер задачи')
                if delete_edit.isdigit():
                    if int(delete_edit) > 0 and int(delete_edit) <= len(collection):
                        removed = collection.pop(int(delete_edit) - 1)
                        show_message("удаление", True, f"— удалена задача «{removed}»")
                    else:
                        show_message("удаление", False, "— задачи с таким номером нет в списке")
                else:
                    show_message("удаление", False, "— введите номер задачи")
            case _:

                show_message("выбор", False, "— такого пункта нет")

    else:
        show_message("выбор", False, "— такого пункта нет")
