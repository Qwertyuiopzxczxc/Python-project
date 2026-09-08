""" Сделал рандом и чтобы печтало какая система и все про нее...
"""

import os
import sys
import platform
import datetime
import random
import shutil

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]
os_platform = platform.platform()
current_time = datetime.datetime.now()
sys_in = sys.path

number = random.randint(1400, 1488)
if number == 1488:
    print("Посхалко")
else:
    print("тебе не повезло!", "тебе выпало число", number)
print(f'Текущая система: {os_name} \n'
      f'Версия система: {os_version} \n'
      f'Архитектура: {os_arch} \n'
      f'Платформа ОС {os_platform} \n'
      f'Дата и время: {current_time} \n')

