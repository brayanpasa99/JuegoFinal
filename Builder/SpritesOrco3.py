from AbstractFactory.Orco import Orco
from Builder.ObtenerSprites import ObtenerSprites


class SpritesOrco3(ObtenerSprites):

    def obtenerSpritesAtacar(self):
        return Orco().Personaje3().Atacar()

    def obtenerSpritesCaminar(self):
        return Orco().Personaje3().Caminar()

    def obtenerSpritesMorir(self):
        return Orco().Personaje3().Muerte()

    def obtenerSpritesCastillo(self):
        return Orco().Castillo().spritesCastillo()
