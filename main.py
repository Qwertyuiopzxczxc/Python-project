from unittest import case

is_running = True
collection = ['task1 "my first task"', 'task2'] # list


print("1 - показать задачи | 2 - добавить заметку")
while is_running:
    print("1 - посмотреть задачи |/n"
              "2 - добавить задачу |/n"
              "3 - выход |/n" )
    print(collection)
    choise_user: str = input("Введите свой выбор")
    match choise_user:
        case "1":
            print(collection)
        case "2":
            collection.append("task")
        case "3":
            for item in enumerate(collection):
                print(key + 1, item)
                select_edit = int(input("Введите номер задачи дляф редактирования"))
                edit_name =input("Укадите новое имя задачи")

            collection.pop(delete_edit - 1)
            is_running = False
            print("покеда")