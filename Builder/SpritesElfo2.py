from AbstractFactory.Elfo import Elfo
from Builder.ObtenerSprites import ObtenerSprites


class SpritesElfo2(ObtenerSprites):

    def obtenerSpritesAtacar(self):
        return Elfo().Personaje2().Atacar()

    def obtenerSpritesCaminar(self):
        return Elfo().Personaje2().Caminar()

    def obtenerSpritesMorir(self):
        return Elfo().Personaje2().Muerte()

    def obtenerSpritesCastillo(self):
        return Elfo().Castillo().spritesCastillo()
