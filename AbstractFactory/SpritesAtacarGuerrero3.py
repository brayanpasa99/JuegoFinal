from AbstractFactory.SpritesGuerrero import SpritesGuerrero
from PersonajesSprites import PersonajesSprites


class SpritesAtacarGuerrero3(SpritesGuerrero):

    def interfaceGuerrero(self):
        _SpritesAtaque = []
        for i in range(0, 8):
            imagen = 'Imagenes/Guerreros/Guerrero3/Ataque/Ataque' + str(i + 1) + '.png'
            _SpritesAtaque.append(PersonajesSprites(imagen))
            return _SpritesAtaque
