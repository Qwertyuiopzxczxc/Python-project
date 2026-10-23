import tkinter as tk
import math

root = tk.Tk()
root.title("Узор из кнопок")
root.geometry("500x500")

n = 12          # количество кнопок
r = 150         # радиус круга
cx, cy = 250, 250
i = 0

while i < n:
    angle = 2 * math.pi * i / n
    x = cx + r * math.cos(angle) - 25
    y = cy + r * math.sin(angle) - 15
    btn = tk.Button(root, text=str(i+1), width=4, height=1)
    btn.place(x=x, y=y)
    i += 1

root.mainloop()
