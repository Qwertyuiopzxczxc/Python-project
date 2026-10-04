# ======================================================
#   Модуль, который отображает информацию пользователю
# ======================================================

def show_collection(task_collection: list) -> None:
    """Красиво выводит список задач в консоль."""
    print("=" * 45)
    if not task_collection:
        print("Список задач пуст!")
    else:
        for number, content in enumerate(task_collection, start=1):
            parts = content.split("|", 1)
            task_name = parts[0].strip()
            task_content = parts[1].strip() if len(parts) > 1 else ""
            print(f"{number}. {task_name}")
            print(f"   Содержание: {task_content}")
    print("=" * 45)


def show_menu() -> None:
    """Выводит меню приложения."""
    print()
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Редактировать задачу")
    print("4 - Удалить задачу")
    print("5 - Выход")
