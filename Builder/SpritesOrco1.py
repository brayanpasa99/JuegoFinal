from AbstractFactory.Orco import Orco
from Builder.ObtenerSprites import ObtenerSprites


class SpritesOrco1(ObtenerSprites):

    def obtenerSpritesAtacar(self):
        return Orco().Personaje1().Atacar()

    def obtenerSpritesCaminar(self):
        return Orco().Personaje1().Caminar()

    def obtenerSpritesMorir(self):
        return Orco().Personaje1().Muerte()

    def obtenerSpritesCastillo(self):
        return Orco().Castillo().spritesCastillo()
