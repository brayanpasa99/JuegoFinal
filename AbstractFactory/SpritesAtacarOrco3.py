from AbstractFactory.SpritesOrco import SpritesOrco
from PersonajesSprites import PersonajesSprites


class SpritesAtacarOrco3(SpritesOrco):

    def interfaceOrco(self):
        _SpritesAtaque = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco3/Ataque/Ataque' + str(i + 1) + '.png'
            _SpritesAtaque.append(PersonajesSprites(imagen))
            return _SpritesAtaque
