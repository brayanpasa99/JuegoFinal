from AbstractFactory.SpritesOrco import SpritesOrco
from PersonajesSprites import PersonajesSprites


class SpritesCaminarOrco3(SpritesOrco):

    def interfaceOrco(self):
        _SpritesCaminar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco3/Caminar/Caminar' + str(i + 1) + '.png'
            _SpritesCaminar.append(PersonajesSprites(imagen))
            return _SpritesCaminar
