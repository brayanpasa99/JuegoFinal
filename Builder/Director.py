from Builder.Caracteristicas import Caracteristicas


class Director():

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCaracteristicas(self):

        caracteristicas = Caracteristicas()

        castillo = self.__builder.obtenerSpritesCastillo()
        iconos = self.__builder.obtenerIconos()
        atacarpersonaje1 = self.__builder.obtenerSpritesAtacarPersonaje1()
        atacarpersonaje2 = self.__builder.obtenerSpritesAtacarPersonaje2()
        atacarpersonaje3 = self.__builder.obtenerSpritesAtacarPersonaje3()
        caminarpersonaje1 = self.__builder.obtenerSpritesCaminarPersonaje1()
        caminarpersonaje2 = self.__builder.obtenerSpritesCaminarPersonaje2()
        caminarpersonaje3 = self.__builder.obtenerSpritesCaminarPersonaje3()
        morirpersonaje1 = self.__builder.obtenerSpritesMorirPersonaje1()
        morirpersonaje2 = self.__builder.obtenerSpritesMorirPersonaje2()
        morirpersonaje3 = self.__builder.obtenerSpritesMorirPersonaje3()

        caracteristicas.setSpritesCastillo(castillo)
        caracteristicas.setIconos(iconos)
        caracteristicas.setSpritesAtacarPersonaje1(atacarpersonaje1)
        caracteristicas.setSpritesAtacarPersonaje2(atacarpersonaje2)
        caracteristicas.setSpritesAtacarPersonaje3(atacarpersonaje3)
        caracteristicas.setSpritesCaminarPersonaje1(caminarpersonaje1)
        caracteristicas.setSpritesCaminarPersonaje2(caminarpersonaje2)
        caracteristicas.setSpritesCaminarPersonaje3(caminarpersonaje3)
        caracteristicas.setSpritesMorirPersonaje1(morirpersonaje1)
        caracteristicas.setSpritesMorirPersonaje2(morirpersonaje2)
        caracteristicas.setSpritesMorirPersonaje3(morirpersonaje3)

        return caracteristicas

