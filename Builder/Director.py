from Builder.Interface import Interface


class Director():

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getInterface(self):

        interface = Interface()
        castillo = self.__builder.obtenerCastillo()
        sprites = self.__builder.obtenerSprites()
        interface.setCastillo(castillo)
        interface.setSprites(sprites)

        return interface

