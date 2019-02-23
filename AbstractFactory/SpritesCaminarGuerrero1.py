from AbstractFactory.SpritesGuerrero import SpritesGuerrero
from PersonajesSprites import PersonajesSprites


class SpritesCaminarGuerrero2(SpritesGuerrero):

    def interfaceGuerrero(self):
        _SpritesCaminar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Guerreros/Guerrero2/Caminar/Caminar' + str(i + 1) + '.png'
            _SpritesCaminar.append(PersonajesSprites(imagen))
            return _SpritesCaminar
