from AbstractFactory.Orco import Orco
from Builder.Constructor import Constructor


class CaracteristicasOrco(Constructor):

    def obtenerSpritesAtacarPersonaje1(self):
        return Orco().Personaje1().Atacar()

    def obtenerSpritesCaminarPersonaje1(self):
        return Orco().Personaje1().Caminar()

    def obtenerSpritesMorirPersonaje1(self):
        return Orco().Personaje1().Muerte()
