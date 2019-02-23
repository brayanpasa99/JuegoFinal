from AbstractFactory.SpritesElfo import SpritesElfo
from PersonajesSprites import PersonajesSprites


class SpritesMorirElfo3(SpritesElfo):

    def interfaceElfo(self):
        _SpritesMuerte = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/Elfo3/Muerte/Muerte' + str(i + 1) + '.png'
            _SpritesMuerte.append(PersonajesSprites(imagen))
            return _SpritesMuerte
