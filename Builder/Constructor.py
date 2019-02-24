import abc


class Constructor():

    @abc.abstractmethod
    def obtenerSpritesCastillo(self):
        pass

    @abc.abstractmethod
    def obtenerIconos(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesAtacarPersonaje1(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesAtacarPersonaje2(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesAtacarPersonaje3(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesCaminarPersonaje1(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesCaminarPersonaje2(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesCaminarPersonaje3(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesMorirPersonaje1(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesMorirPersonaje2(self):
        pass

    @abc.abstractmethod
    def obtenerSpritesMorirPersonaje3(self):
        pass
