from AbstractFactory.Orco1 import Orco1
from AbstractFactory.Orco2 import Orco2
from AbstractFactory.Orco3 import Orco3
from AbstractFactory.Personajes import Personajes


class Orco(Personajes):

    def Personaje1(self):
        return Orco1()

    def Personaje2(self):
        return Orco2()

    def Personaje3(self):
        return Orco3()
