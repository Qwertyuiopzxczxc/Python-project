import tkinter as tk
class AppButton(tk.Button):
    def __init__(self,master, text,command=None,width=20,height=2):
        super().__init__( master,text=text,command=command,width=width,height=height)
        self.pack(pady=5)
