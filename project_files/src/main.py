"""
Точка входа в приложение Task Manager.
Слоистая архитектура (Урок 13–14).

Версия: 0.2.0
"""

from ui.interface import Interface


def main():
    app = Interface()
    app.run()


if __name__ == "__main__":
    main()