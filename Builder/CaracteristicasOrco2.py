from AbstractFactory.Orco import Orco
from Builder.Constructor import Constructor


class CaracteristicasOrco(Constructor):

    def obtenerSpritesAtacarPersonaje2(self):
        return Orco().Personaje2().Atacar()

    def obtenerSpritesCaminarPersonaje2(self):
        return Orco().Personaje2().Caminar()

    def obtenerSpritesMorirPersonaje2(self):
        return Orco().Personaje2().Muerte()
