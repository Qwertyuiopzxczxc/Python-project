import tkinter as tk

# 1. Tkinter уже входит в стандартную библиотеку Python,
#    но если вдруг его нет — установите: pip install tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("320x420")
root.resizable(False, False)

# Поле для вывода (пункт 4 справа)
text_input = tk.Label(
    root,
    text="",
    font=("Arial", 24),
    bg="#222",
    fg="white",
    anchor="e",
    padx=10,
    pady=15
)
text_input.pack(fill="x", padx=10, pady=10)

# Переменная для хранения текущего выражения
expression = ""

# Функция, которая обрабатывает нажатия (пункты 5 и 6)
def button_click(value):
    global expression

    if value == "=":
        try:
            # Заменяем % на /100 для процентов
            result = str(eval(expression.replace("%", "/100")))
            text_input.config(text=result)
            expression = result
        except:
            text_input.config(text="Ошибка")
            expression = ""
    else:
        expression += str(value)
        text_input.config(text=expression)

# 2. Создаём 10 кнопок с цифрами 0–9
digits = ["7", "8", "9",
          "4", "5", "6",
          "1", "2", "3",
          "0"]

digit_frame = tk.Frame(root)
digit_frame.pack(pady=5)

row = 0
col = 0
for digit in digits:
    btn = tk.Button(
        digit_frame,
        text=digit,
        font=("Arial", 16),
        width=5,
        height=2,
        command=lambda d=digit: button_click(d)
    )
    btn.grid(row=row, column=col, padx=3, pady=3)

    col += 1
    if col > 2:
        col = 0
        row += 1

# 3. Массив знаков арифметических операций
operations = ["*", "%", "+", "-", "="]

# 4. Создаём 5 кнопок операций через цикл for
op_frame = tk.Frame(root)
op_frame.pack(pady=5)

for op in operations:
    btn = tk.Button(
        op_frame,
        text=op,
        font=("Arial", 16),
        width=5,
        height=2,
        bg="#444",
        fg="white",
        command=lambda o=op: button_click(o)
    )
    btn.pack(side="left", padx=3)

# Кнопка очистки (дополнительно, чтобы было удобно)
clear_btn = tk.Button(
    root,
    text="C",
    font=("Arial", 14),
    width=28,
    height=1,
    bg="#aa3333",
    fg="white",
    command=lambda: (globals().update(expression=""), text_input.config(text=""))
)
clear_btn.pack(pady=10)

root.mainloop()
