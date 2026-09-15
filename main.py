"""## Версия 0.0.4

    Точка входа в пиложение Task Manadger
    --- decsription ---
    приложение сохраняет
"""

collection = ['1','2'] #list

task_number = 0

is_start = True #flag

def listcheck(task_collection, name):
    if name in task_collection:
        print('Такая задача уже есть')
        exit()
    else:
        pass
def show_collection(task_collection):
    print('=' * 30)
    for task_number, j in enumerate(collection):
        print(f"{task_number + 1}. {j}")
    print('=' * 30)

while is_start:

    print("1 - показать задачи | 2 - добавить задачу | 3 - редактировать задачу | 4 - удалить задачу")

    choice_user = input('Введите ваш выбор ( 1 | 2 | 3 | 4 )')

    if choice_user == '1' or choice_user == '2' or choice_user == '3' or choice_user == '4':
        match int(choice_user):

            case 1:
                show_collection(collection)
            case 2:
                task_name = input('Название задачи (или оставьте пустым): ')
                match (task_name):
                    case "":
                        task_name: str = 'task'
                        task_number += 1
                        collection.append(f"{task_name} {task_number}")
                    case _:
                        listcheck(collection,task_name)
                        collection.append(f"{task_name}")
            case 3:
                show_collection(collection)
                select_edit = (input('введите номер задачи'))
                if int(select_edit.isdigit()):
                    if int(select_edit) > 0 and int(select_edit) <= len(collection):
                        edit_name = input('новое имя задачи')
                        collection[int(select_edit)] = edit_name
                        print(f"задача '{int(select_edit)}' '{edit_name}' успешно отредактированна!")
                    else:
                        print('Задачи с таким номером нет в списке')
                else:
                    print('!!!')


            case 4:
                show_collection(collection)
                delete_edit = input('введите номер задачи')
                if int(delete_edit.isdigit()):
                    if int(delete_edit) > 0 and int(delete_edit) <= len(collection):
                        collection.pop(int(delete_edit))
                    else:
                        print('Задачи с таким номером нет в списке')
                else:
                    print('Введите номер задачи!!!')
            case _:

                print('такого пункта нет!')

    elif choice_user != '1' or choice_user != '2' or choice_user != '3' or choice_user != '4':
        pass