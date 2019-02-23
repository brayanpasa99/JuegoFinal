import abc


class Personaje():
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def SpritesAtacar(self):
        pass

    @abc.abstractmethod
    def SpritesCaminar(self):
        pass

    @abc.abstractmethod
    def SpritesMuerte(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def dibujar(self):
        pass
