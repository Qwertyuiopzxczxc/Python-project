import tkinter as tk

a = 0
b = 0

def multiply():
    pass

def sum():
    pass

def diff():
    pass

def divide():
    pass

def result():
    pass

root = tk.Tk()

root.geometry("350x500")
root.iconbitmap("../assets/icon.ico")

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

states =[['multiply', '*'], ['sum','+'],['diff', '-'],['divide', '%'],['result', '=']]
for state in states:
    b=(tk.Button(footer))
    b.pack(side='right')
    b.config(command=state[0],text=state[1])

label = tk.Label(header, text=" ")
label.pack(side='left')

result_text = tk.Label(header, text=" ")
result_text.pack(side='right')
root.mainloop()
