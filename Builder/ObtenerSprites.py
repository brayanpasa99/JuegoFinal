import abc


class ObtenerSprites():

    @abc.abstractmethod
    def obtenerSpritesAtacar(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesCaminar(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesMorir(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesCastillo(self):
        pass
