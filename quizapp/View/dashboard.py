from tkinter import *
from Enum.screen import Screen


class Dashboard(Frame):
    def __init__(self, parent, controller, params=None):
        super().__init__(parent)
        self.controller = controller

        label_username = Label(self, text=f"Welcome {params['username']}", font=("Arial", 12))
        label_username.grid(row=0, column=2)

        # create 6 square buttons with dummy text
        button1 = Button(self, text="Button 1", width=10, height=5)
        button1.grid(row=1, column=1)

        button2 = Button(self, text="Button 2", width=10, height=5)
        button2.grid(row=1, column=2)

        button3 = Button(self, text="Button 3", width=10, height=5)
        button3.grid(row=1, column=3)

        button4 = Button(self, text="Button 4", width=10, height=5)
        button4.grid(row=2, column=3)

        button5 = Button(self, text="Button 5", width=10, height=5)
        button5.grid(row=2, column=1)

        button6 = Button(self, text="Button 6", width=10, height=5)
        button6.grid(row=2, column=2)

        button6 = Button(self, text="logout", width=2, height=1, command=self.logout)
        button6.grid(row=3, column=0)

    def logout(self):
        self.controller.show_frame(Screen.login, self.controller)
        self.destroy()
