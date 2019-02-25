from AbstractFactory.Orco import Orco
from Builder.ObtenerSprites import ObtenerSprites


class SpritesOrco2(ObtenerSprites):

    def obtenerSpritesAtacar(self):
        return Orco().Personaje2().Atacar()

    def obtenerSpritesCaminar(self):
        return Orco().Personaje2().Caminar()

    def obtenerSpritesMorir(self):
        return Orco().Personaje2().Muerte()

    def obtenerSpritesCastillo(self):
        return Orco().Castillo().spritesCastillo()
