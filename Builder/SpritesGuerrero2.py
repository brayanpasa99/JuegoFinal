from AbstractFactory.Guerrero import Guerrero
from Builder.ObtenerSprites import ObtenerSprites


class SpritesGuerrero2(ObtenerSprites):

    def obtenerSpritesAtacar(self):
        return Guerrero().Personaje2().Atacar()

    def obtenerSpritesCaminar(self):
        return Guerrero().Personaje2().Caminar()

    def obtenerSpritesMorir(self):
        return Guerrero().Personaje2().Muerte()

    def obtenerSpritesCastillo(self):
        return Guerrero().Castillo().spritesCastillo()
