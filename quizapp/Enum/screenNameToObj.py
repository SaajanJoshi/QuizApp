from enum import Enum
from View import Login, Dashboard, StartPage


class ScreenToObj(Enum):
    login = ["login", Login]
    dashboard = ["dashboard", Dashboard]
    startPage =["startPage", StartPage]

    @staticmethod
    def getScreen(name):
        for screen in ScreenToObj:
            if screen.value[0] == name:
                return screen.value[1]
