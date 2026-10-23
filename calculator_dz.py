import tkinter as tk

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

expression = ""

def button_click(value):
    global expression

    if value == "=":
        try:

            result = str(eval(expression.replace("%", "/100")))
            text_input.config(text=result)
            expression = result
        except:
            text_input.config(text="Ошибка")
            expression = ""
    else:
        expression += str(value)
        text_input.config(text=expression)


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


operations = ["*", "%", "+", "-", "="]

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
