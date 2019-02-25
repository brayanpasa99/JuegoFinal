from AbstractFactory.Guerrero import Guerrero
from Builder.ObtenerSprites import ObtenerSprites


class SpritesGuerrero1(ObtenerSprites):

    def obtenerSpritesAtacar(self):
        return Guerrero().Personaje1().Atacar()

    def obtenerSpritesCaminar(self):
        return Guerrero().Personaje1().Caminar()

    def obtenerSpritesMorir(self):
        return Guerrero().Personaje1().Muerte()

    def obtenerSpritesCastillo(self):
        return Guerrero().Castillo().spritesCastillo()
