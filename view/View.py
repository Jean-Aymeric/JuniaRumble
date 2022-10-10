from model.model import Model


class View:
    def __init__(self, controller, model):
        self.__controller = None
        self.__model = None

    def setController(self, controller):
        self.__controller = controller

    def setModel(self, model):
        self.__model = model

