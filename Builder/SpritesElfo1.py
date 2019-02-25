from AbstractFactory.Elfo import Elfo
from Builder.ObtenerSprites import ObtenerSprites


class SpritesElfo1(ObtenerSprites):

    def obtenerSpritesAtacar(self):
        return Elfo().Personaje1().Atacar()

    def obtenerSpritesCaminar(self):
        return Elfo().Personaje1().Caminar()

    def obtenerSpritesMorir(self):
        return Elfo().Personaje1().Muerte()

    def obtenerSpritesCastillo(self):
        return Elfo().Castillo().spritesCastillo()
