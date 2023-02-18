from tkinter import *
from Configs import log
from Enum.screen import Screen
from Enum.screenNameToObj import ScreenToObj


class Root(Tk):
    def __init__(self):
        super().__init__()
        container = Frame(self, width=600, height=600)
        container.grid(row=0, column=0)

        self.title('Quiz Application')
        log.info('Application Started')
        self.show_frame(Screen.start, container)

    def show_frame(self, view, main_container, params=None):
        view = ScreenToObj.getScreen(view.value)
        frame = view(parent=main_container, controller=self, params=params)
        frame.grid(row=0, column=0, sticky=N)


if __name__ == "__main__":
    app = Root()
    app.mainloop()
