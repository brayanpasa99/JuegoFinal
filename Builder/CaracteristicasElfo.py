from AbstractFactory.Elfo import Elfo
from Builder.Constructor import Constructor


class CaracteristicasElfo(Constructor):

    def obtenerCastillo(self):
        return Elfo().Castillo()

    def obtenerPersonaje1(self):
        return Elfo().Personaje1()

    def obtenerPersonaje2(self):
        return Elfo().Personaje2()

    def obtenerPersonaje3(self):
        return Elfo().Personaje3()
