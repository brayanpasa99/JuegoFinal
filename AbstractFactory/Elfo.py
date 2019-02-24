from AbstractFactory.Elfo1 import Elfo1
from AbstractFactory.Elfo2 import Elfo2
from AbstractFactory.Elfo3 import Elfo3
from AbstractFactory.Personajes import Personajes


class Elfo(Personajes):

    def Personaje1(self):
        return Elfo1()

    def Personaje2(self):
        return Elfo2()

    def Personaje3(self):
        return Elfo3()
