from AbstractFactory.CastilloGuerrero import CastilloGuerrero
from AbstractFactory.Guerrero1 import Guerrero1
from AbstractFactory.Guerrero2 import Guerrero2
from AbstractFactory.Guerrero3 import Guerrero3
from AbstractFactory.Personajes import Personajes


class Guerrero(Personajes):

    def Personaje1(self):
        return Guerrero1()

    def Personaje2(self):
        return Guerrero2()

    def Personaje3(self):
        return Guerrero3()

    def Castillo(self):
        return CastilloGuerrero()
