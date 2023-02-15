from tkinter import *
from View.start import StartPage
from Configs import log


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('650x650')
        self.title('Quiz Application')
        log.info('Application Started')
        log.info('Start Page')

        view = StartPage(self)
        view.grid(row=0, column=0)


if __name__ == "__main__":
    app = Root()
    app.mainloop()
