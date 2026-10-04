# ======================================================
#              Модуль, содержащий утилиты
# ======================================================

def check_confirm(select_task: str, task_list: list) -> bool:
    """
    Проверяет, что введённый номер задачи корректный.
    Возвращает True, если номер валидный, иначе False.
    """
    if not select_task.isdigit():
        print("Введите именно номер задачи!")
        return False

    number = int(select_task)
    if 0 < number <= len(task_list):
        return True

    print(f"Задачи с номером {select_task} нет в списке!")
    return False
