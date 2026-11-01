"""
Модуль конфигурации приложения.
Версия: 0.2.0
"""

import os
from utils import get_base_dir

# Имя файла сохранения (JSON) — лежит рядом с папкой src
_base = get_base_dir()
NAME_FILE_SAVES = os.path.abspath(os.path.join(_base, "..", "saves.json"))

# Размеры окна
WINDOW_WIDTH = 520
WINDOW_HEIGHT = 480

# Цвета
COLOR_BG_DARK = "#1e1e2e"
COLOR_BG_FRAME = "#2a2a3d"
COLOR_ACCENT = "#4a6cf7"
COLOR_TEXT = "#e0e0e0"
COLOR_BUTTON = "#3b5bdb"
COLOR_BUTTON_HOVER = "#5c7cfa"
