import abc

class CastilloAbstracto():

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def spritesCastillo(self):
        pass

    @abc.abstractmethod
    def spritesIconos(self):
        pass

    @abc.abstractmethod
    def coordenadas(self, jugador1, x, y):
        pass
