from tkinter import *
from Configs import log
from PIL import ImageTk, Image
from .login import Login


class StartPage(Frame):
    def __init__(self, parent, controller, params=None):
        super().__init__(parent)
        self.parent = parent
        self.params = params
        self.controller = controller
        self.photo = ImageTk.PhotoImage(Image.open("Resources/quiz.jpg")
                                        .resize((650, 600), Image.ANTIALIAS))

        label = Label(self, image=self.photo)
        label.grid()

        login_button = Button(self, text="Continue to Login", command=self.login_screen)
        login_button.grid(row=1, column=0, sticky='w')

        continue_as_guest = Button(self, text="Continue to as Guest", command=self.guest_screen)
        continue_as_guest.grid(row=1, column=0, sticky='e')

    def login_screen(self):
        log.info("Login button pressed")
        self.controller.show_frame(Login, self.controller)
        self.destroy()


    def guest_screen(self):
        log.info("guest button pressed")
        pass
