from AbstractFactory.SpritesElfo import SpritesElfo
from PersonajesSprites import PersonajesSprites


class SpritesAtacarElfo1(SpritesElfo):

    def interfaceElfo(self):

        _SpritesAtaque = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/Elfo1/Ataque/Ataque' + str(i + 1) + '.png'

            _SpritesAtaque.append(PersonajesSprites(imagen))
            return _SpritesAtaque

