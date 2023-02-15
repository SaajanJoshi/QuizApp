from tkinter import *
from Configs import log
from PIL import ImageTk, Image


class StartPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.photo = ImageTk.PhotoImage(Image.open("Resources/quiz.jpg")
                                        .resize((650, 600), Image.ANTIALIAS))

        self.label = Label(self, image=self.photo)
        self.label.grid(row=0, column=0)

        self.login_button = Button(self, text="Continue to Login", command=self.login_screen)
        self.login_button.grid(sticky="w", row=1, column=0)

        self.continue_as_guest = Button(self, text="Continue to as Guest", command=self.guest_screen)
        self.continue_as_guest.grid(sticky="e", row=1, column=0)

    def login_screen(self):
        log.info("Login button pressed")
        pass

    def guest_screen(self):
        log.info("guest button pressed")
        pass
