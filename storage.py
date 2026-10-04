# ===========================================================
#      Модуль, который загружает и сохраняет задачи
# ===========================================================

def save_tasks(task_collection: list, name_file: str) -> None:
    """Сохраняет список задач в файл."""
    with open(name_file, "w", encoding="utf-8") as file:
        for task in task_collection:
            file.write(task.rstrip("\n") + "\n")


def load_tasks(name_file: str) -> list:
    """Загружает список задач из файла."""
    try:
        with open(name_file, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []
