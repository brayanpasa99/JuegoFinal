from AbstractFactory.Guerrero import Guerrero
from Builder.Constructor import Constructor


class CaracteristicasGuerrero(Constructor):

    def obtenerSpritesCastillo(self):
        return Guerrero().Castillo().spritesCastillo()

    def obtenerIconos(self):
        return Guerrero().Castillo().spritesIconos()

    def obtenerSpritesAtacarPersonaje1(self):
        return Guerrero().Personaje1().Atacar()

    def obtenerSpritesAtacarPersonaje2(self):
        return Guerrero().Personaje2().Atacar()

    def obtenerSpritesAtacarPersonaje3(self):
        return Guerrero().Personaje3().Atacar()

    def obtenerSpritesCaminarPersonaje1(self):
        return Guerrero().Personaje1().Caminar()

    def obtenerSpritesCaminarPersonaje2(self):
        return Guerrero().Personaje2().Caminar()

    def obtenerSpritesCaminarPersonaje3(self):
        return Guerrero().Personaje3().Caminar()

    def obtenerSpritesMorirPersonaje1(self):
        return Guerrero().Personaje1().Muerte()

    def obtenerSpritesMorirPersonaje2(self):
        return Guerrero().Personaje2().Muerte()

    def obtenerSpritesMorirPersonaje3(self):
        return Guerrero().Personaje3().Muerte()
