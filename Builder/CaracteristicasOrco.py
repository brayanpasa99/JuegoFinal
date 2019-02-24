from AbstractFactory.Orco import Orco
from Builder.Constructor import Constructor


class CaracteristicasOrco(Constructor):

    def obtenerSpritesCastillo(self):
        return Orco().Castillo().spritesCastillo()

    def obtenerIconos(self):
        return Orco().Castillo().spritesIconos()

    def obtenerSpritesAtacarPersonaje1(self):
        return Orco().Personaje1().Atacar()

    def obtenerSpritesAtacarPersonaje2(self):
        return Orco().Personaje2().Atacar()

    def obtenerSpritesAtacarPersonaje3(self):
        return Orco().Personaje3().Atacar()

    def obtenerSpritesCaminarPersonaje1(self):
        return Orco().Personaje1().Caminar()

    def obtenerSpritesCaminarPersonaje2(self):
        return Orco().Personaje2().Caminar()

    def obtenerSpritesCaminarPersonaje3(self):
        return Orco().Personaje3().Caminar()

    def obtenerSpritesMorirPersonaje1(self):
        return Orco().Personaje1().Muerte()

    def obtenerSpritesMorirPersonaje2(self):
        return Orco().Personaje2().Muerte()

    def obtenerSpritesMorirPersonaje3(self):
        return Orco().Personaje3().Muerte()
