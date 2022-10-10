from model.model import Model
from view.View import View


class Controller:
    __model: Model
    __view: View

    def __init__(self, model, view):
        self.__model = model
        self.__view = view
        self.__model.setController(self)
        self.__view.setController(self)
        self.__view.setModel(self.__model)
