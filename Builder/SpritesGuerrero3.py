from AbstractFactory.Guerrero import Guerrero
from Builder.ObtenerSprites import ObtenerSprites


class SpritesGuerrero3(ObtenerSprites):

    def obtenerSpritesAtacar(self):
        return Guerrero().Personaje3().Atacar()

    def obtenerSpritesCaminar(self):
        return Guerrero().Personaje3().Caminar()

    def obtenerSpritesMorir(self):
        return Guerrero().Personaje3().Muerte()

    def obtenerSpritesCastillo(self):
        return Guerrero().Castillo().spritesCastillo()
