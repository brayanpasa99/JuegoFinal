from Builder.Sprites import Sprites


class Director():

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getSprites(self):

        SpritesPersonaje = Sprites()

        atacar = self.__builder.obtenerSpritesAtacar()
        caminar = self.__builder.obtenerSpritesCaminar()
        morir = self.__builder.obtenerSpritesMorir()
        castillo = self.__builder.obtenerSpritesCastillo()

        SpritesPersonaje.setSpritesAtacar(atacar)
        SpritesPersonaje.setSpritesCaminar(caminar)
        SpritesPersonaje.setSpritesMorir(morir)
        SpritesPersonaje.setSpritesCastillo(castillo)

        return SpritesPersonaje

