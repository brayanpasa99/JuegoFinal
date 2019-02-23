from AbstractFactory.SpritesElfo import SpritesElfo
from PersonajesSprites import PersonajesSprites


class SpritesAtacarElfo3(SpritesElfo):

    def interfaceElfo(self):
        _SpritesAtaque = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/Elfo3/Ataque/Ataque' + str(i + 1) + '.png'
            _SpritesAtaque.append(PersonajesSprites(imagen))
            return _SpritesAtaque
