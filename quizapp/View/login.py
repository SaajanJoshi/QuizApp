from tkinter import *
from Enum import Error, Credential


class Login(Frame):
    def __init__(self, parent, controller, params=None):

        super().__init__(parent)
        self.params = params
        self.password = None
        self.username = None
        self.controller = controller

        label = Label(self, text="Username:", font=("Arial", 12))
        label.grid(row=0, column=0)

        entry_username = Entry(self, font=("Arial", 12))
        entry_username.focus()
        entry_username.grid(row=1, column=0)

        label_password = Label(self, text="Password:", font=("Arial", 12))
        label_password.grid(row=2, column=0)

        entry_password = Entry(self, show="*", font=("Arial", 12))
        entry_password.grid(row=3, column=0)

        button_login = Button(self, text="Login", font=("Arial", 12),
                              command=lambda: self.login(entry_username.get(), entry_password.get()))
        button_login.grid(row=4, column=0)

    def login(self, username, password):
        from .dashboard import Dashboard
        self.username = username
        self.password = password
        if Credential.USERNAME.value == self.username and Credential.PASSWORD.value == self.password:
            self.controller.show_frame(Dashboard, self.controller,
                                       {'username': self.username, 'password': self.password})
            self.destroy()
        else:
            error_label = Label(self, text=Error.INVALID_USER_PASSWORD.value, font=("Arial", 12), bg="red")
            error_label.grid(row=5, column=0)
