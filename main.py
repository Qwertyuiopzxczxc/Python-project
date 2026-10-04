"""
=== Основной файл приложения Task Manager ===

Версия: 0.1.0

=== История улучшений по версиям ===

0.0.1
    - Создан базовый проект и основной цикл программы.

0.0.2
    - Добавлено хранение задач в списке.
    - Реализован показ и добавление задач.

0.0.3
    - Добавлены сохранение в файл, редактирование и удаление задач.

0.0.4 – 0.0.6
    - Улучшена логика работы с файлом.
    - Добавлены первые проверки пользовательского ввода.
    - Начало рефакторинга.

0.0.7
    - Стабильная версия с полным набором функций
      (показать / добавить / редактировать / удалить / сохранить).

0.0.8
    - Начало разбиения кода на модули.

0.0.9
    - Созданы модули:
        • view.py     — отображение меню и списка задач
        • utils.py    — проверка корректности номера задачи
        • core.py     — основная бизнес-логика
        • storege.py  — сохранение и загрузка (с опечаткой)
    - Добавлен config.py

0.1.0
    - Исправлены все найденные баги (см. BUGFIX.md)
    - Переименован storege.py → storage.py
    - Убраны лишние \n в данных задач
    - Удалены ненужные файлы (os.py, processes.py)
    - Улучшена структура main.py
    - Добавлена полная документация версий
    - Приложение работает стабильно в модульной архитектуре
"""

from storage import load_tasks, save_tasks
from view import show_menu, show_collection
from core import add_task, edit_task, delete_tasks
from config import NAME_FILE_SAVES


def main():
    """Главная функция приложения."""
    name_file = NAME_FILE_SAVES
    collection = load_tasks(name_file)

    is_running = True

    while is_running:
        show_menu()
        choice_user = input("Введите ваш выбор: ").strip()

        match choice_user:
            case "1":
                show_collection(collection)

            case "2":
                add_task(collection)
                save_tasks(collection, name_file)

            case "3":
                show_collection(collection)
                edit_task(collection)
                save_tasks(collection, name_file)

            case "4":
                show_collection(collection)
                delete_tasks(collection)
                save_tasks(collection, name_file)

            case "5":
                save_tasks(collection, name_file)
                is_running = False
                print("До свидания!")

            case _:
                print("Такого пункта нет...")


if __name__ == "__main__":
    main()
