import tkinter as tk
from itertools import count

numbers = ''

def add_number(char):
    global numbers
    numbers += str(char)
    label.config(text=numbers)


def handle_operation(sign):
    global numbers

    if sign == '=':
        try:
            result = eval(numbers)
            result_text.config(text=result)
            numbers = str(result)

        except Exception as error:
            print("Ошибка в выражении!")
            numbers = ''

    else:
        numbers += sign
        label.config(text=numbers)



root = tk.Tk()

root.geometry("350x500")


frame = tk.Frame(root)
frame.pack()

header = tk.Frame(root, bg="grey", padx=10, pady=10)
header.pack(side="top", fill="x")

footer = tk.Frame(root, bg="black", padx=10, pady=10)
footer.pack(side="bottom", fill="x")



list_button = []

for i in range(10):
    b = (tk.Button(footer))
    b.pack(side='left')
    b.config(text=str(i))
    b.config(command=lambda char=i: add_number(char))


states =[['multiply', '*'], ['sum','+'],['diff', '-'],['divide', '%'],['result', '=']]
for state in states:
    b = tk.Button(footer)
    b.pack(side='right')
    b.config(
        text=state[1],
        command=lambda sign=state[1]: handle_operation(sign)
    )

label = tk.Label(header, text=" ")
label.pack(side='left')

result_text = tk.Label(header, text=" ")
result_text.pack(side='right')
root.mainloop()
