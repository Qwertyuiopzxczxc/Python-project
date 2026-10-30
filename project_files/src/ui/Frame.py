import tkinter as tk

class AppFrame(tk.Frame):
    def __init__(self, master,color,width,height):
        super().__init__(master, bg=color, width=width,height=height)
        self.background = color
        self.master = master
        self.width = width
        self.height = height
        self.pack_propagate(False)
        self.pack()

    def hide(self, event: bool):
        if event: self.pack_forget()
        else: self.pack()

class AppButton(tk.Button):
    def __init__(self,master, text,command=None,width=20,height=2):
        super().__init__( master,text=text,command=command,width=width,height=height)
        self.pack(pady=5)