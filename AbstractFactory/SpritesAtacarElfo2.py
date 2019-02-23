from AbstractFactory.SpritesElfo import SpritesElfo
from PersonajesSprites import PersonajesSprites


class SpritesAtacarElfo2(SpritesElfo):

    def interfaceElfo(self):
        _SpritesAtaque = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/Elfo2/Ataque/Ataque' + str(i + 1) + '.png'
            _SpritesAtaque.append(PersonajesSprites(imagen))
            return _SpritesAtaque


