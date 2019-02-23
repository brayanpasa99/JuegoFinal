from AbstractFactory.SpritesGuerrero import SpritesGuerrero
from PersonajesSprites import PersonajesSprites


class SpritesMorirGuerrero2(SpritesGuerrero):

    def interfaceGuerrero(self):
        _SpritesMuerte = []
        for i in range(0, 7):
            imagen = 'Imagenes/Guerreros/Guerrero2/Muerte/Muerte' + str(i + 1) + '.png'
            _SpritesMuerte.append(PersonajesSprites(imagen))
            return _SpritesMuerte
