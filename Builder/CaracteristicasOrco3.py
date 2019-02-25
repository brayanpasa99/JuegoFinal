from AbstractFactory.Orco import Orco
from Builder.Constructor import Constructor


class CaracteristicasOrco(Constructor):

    '''def obtenerSpritesCastillo(self):
        return Orco().Castillo().spritesCastillo()

    def obtenerIconos(self):
        return Orco().Castillo().spritesIconos()'''

    def obtenerSpritesAtacarPersonaje3(self):
        return Orco().Personaje3().Atacar()

    def obtenerSpritesCaminarPersonaje3(self):
        return Orco().Personaje3().Caminar()

    def obtenerSpritesMorirPersonaje3(self):
        return Orco().Personaje3().Muerte()
