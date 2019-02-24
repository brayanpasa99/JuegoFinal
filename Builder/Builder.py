import abc
from Builder.Product import Product


class Builder():

    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def obtenerCastillo(self):
        pass

    @abc.abstractmethod
    def obtenerSprites(self):
        pass
