from AbstractFactory.Elfo import Elfo
from Builder.Constructor import Constructor


class CaracteristicasElfo(Constructor):

    def obtenerSpritesCastillo(self):
        return Elfo().Castillo().spritesCastillo()

    def obtenerIconos(self):
        return Elfo().Castillo().spritesIconos()

    def obtenerSpritesAtacarPersonaje1(self):
        return Elfo().Personaje1().Atacar()

    def obtenerSpritesAtacarPersonaje2(self):
        return Elfo().Personaje2().Atacar()

    def obtenerSpritesAtacarPersonaje3(self):
        return Elfo().Personaje3().Atacar()

    def obtenerSpritesCaminarPersonaje1(self):
        return Elfo().Personaje1().Caminar()

    def obtenerSpritesCaminarPersonaje2(self):
        return Elfo().Personaje2().Caminar()

    def obtenerSpritesCaminarPersonaje3(self):
        return Elfo().Personaje3().Caminar()

    def obtenerSpritesMorirPersonaje1(self):
        return Elfo().Personaje1().Muerte()

    def obtenerSpritesMorirPersonaje2(self):
        return Elfo().Personaje2().Muerte()

    def obtenerSpritesMorirPersonaje3(self):
        return Elfo().Personaje3().Muerte()
