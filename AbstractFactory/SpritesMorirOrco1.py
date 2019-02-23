from AbstractFactory.SpritesOrco import SpritesOrco
from PersonajesSprites import PersonajesSprites


class SpritesMorirOrco1(SpritesOrco):

    def interfaceOrco(self):
        _SpritesMuerte = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco1/Muerte/Muerte' + str(i + 1) + '.png'
            _SpritesMuerte.append(PersonajesSprites(imagen))
            return _SpritesMuerte
