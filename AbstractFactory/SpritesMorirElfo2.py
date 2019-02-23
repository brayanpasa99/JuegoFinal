from AbstractFactory.SpritesElfo import SpritesElfo
from PersonajesSprites import PersonajesSprites


class SpritesMorirElfo2(SpritesElfo):

    def interfaceElfo(self):
        _SpritesMuerte = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/Elfo2/Muerte/Muerte' + str(i + 1) + '.png'
            _SpritesMuerte.append(PersonajesSprites(imagen))
            return _SpritesMuerte
