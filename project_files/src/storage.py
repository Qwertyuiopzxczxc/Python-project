"""
                                === Функции для сохранения и загрузки ===

                                    === Версия приложения: 0.0.9 ===
"""
import json

### Сохранение задач
def load_file(task_list, file_name):
    if not
    with open(file_name, "r", encoding="utf-8") as file:
        task_list = json.loads(file.read())

### Загрузка задач
def load_tasks(name_file):
    try:
        with open(name_file, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []