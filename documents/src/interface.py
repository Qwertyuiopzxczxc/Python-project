import tkinter as tk

score = 0

def start():
    global score
    score += 1
    label.config(text=str(score))

root = tk.Tk()

root.geometry("500x500")
root.iconbitmap("../assets/icon.ico")

header = tk.Frame(root, bg="black", width=100, height=300)
header.pack(side="top", fill="x")

footer = tk.Frame(root, bg="white", width=100, height=300)
footer.pack(side="bottom", fill="x")

main = tk.Frame(root, bg="yellow", width=400, height=400)
main.pack(side="bottom", fill="x")

label = tk.Label(header,text="Hello World", height=2, width=10)
label.pack()

entry = tk.Entry(header)
entry.pack()


root.mainloop()
