from AbstractFactory.SpritesElfo import SpritesElfo
from PersonajesSprites import PersonajesSprites


class SpritesCaminarElfo1(SpritesElfo):

    def interfaceElfo(self):
        _SpritesCaminar = []
        for i in range(0, 3):
            imagen = 'Imagenes/Elfos/Elfo1/Caminar/Caminar' + str(i + 1) + '.png'
            _SpritesCaminar.append(PersonajesSprites(imagen))
            return _SpritesCaminar
