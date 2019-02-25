from AbstractFactory.Elfo import Elfo
from Builder.ObtenerSprites import ObtenerSprites


class SpritesElfo3(ObtenerSprites):

    def obtenerSpritesAtacar(self):
        return Elfo().Personaje3().Atacar()

    def obtenerSpritesCaminar(self):
        return Elfo().Personaje3().Caminar()

    def obtenerSpritesMorir(self):
        return Elfo().Personaje3().Muerte()

    def obtenerSpritesCastillo(self):
        return Elfo().Castillo().spritesCastillo()
