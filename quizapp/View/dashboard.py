from tkinter import *


class Dashboard(Frame):
    def __init__(self, parent, controller, params=None):
        super().__init__(parent)
        self.controller = controller

        label_username = Label(self, text=f"Welcome {params['username']}", font=("Arial", 12))
        label_username.grid(row=0, column=0, sticky=N)
