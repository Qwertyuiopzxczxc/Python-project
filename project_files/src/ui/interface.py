import tkinter as tk
from Frame import AppFrame
from Button import AppButton
class Interface:
    def __init__(self, window_w = 400, window_h = 400):
        self.root = tk.Tk()

        self.root_w = window_w
        self.root_h = window_h
        self.root.geometry(f"{self.root_w}x{self.root_h}")
        self.root.iconbitmap("../assets/icon.ico")

        self.frames = {}
        self.buttons = []

        self.create_interface()

    def create_interface(self):
        self.create_frames(["menu","tasks"])
        self.create_buttons()

    def create_frames(self, name_frame):
        c = ["black", "grey"]
        for i in range(len(name_frame)):
            frame = AppFrame(self.root, c[i], self.root_w, self.root_h)
            self.frames[name_frame[i]] = frame
        print(self.frames)

    def create_buttons(self,):
        button_show_tasks = tk.Button(self.frames["menu"],text="Посмотреть все задачи", width=20, height=3, command=lambda: self.command_quit("menu", True))
        button_to_menu = AppButton(self.frames["tasks"], color="blue", text="Вернуться в меню", width=20, height=3, command=lambda: self.command_quit("tasks",True))

    def add_listbox(self, name_frame):
        lb = Listbox(self.frames[name_frame])
        self.listbox = lb

    def command_quit(self,name_frame,flag):
        if flag and name_frame == 'menu':
            self.frames["menu"].hide(True)
            self.frames["tasks"].hide(False)

        elif flag and name_frame == 'tasks':
            self.frames["tasks"].hide(True)
            self.frames["menu"].hide(False)