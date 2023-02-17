from tkinter import *
from Configs import log
from View import StartPage


class Root(Tk):
    def __init__(self):
        super().__init__()
        container = Frame(self, width=600, height=600)
        container.grid(row=0, column=0)

        self.title('Quiz Application')
        log.info('Application Started')
        self.show_frame(StartPage, container)

    def show_frame(self, view, main_container, params=None):
        '''Show a frame for the given page name'''
        frame = view(parent=main_container, controller=self, params=params)
        frame.grid(row=0, column=0, sticky=N)


if __name__ == "__main__":
    app = Root()
    app.mainloop()
