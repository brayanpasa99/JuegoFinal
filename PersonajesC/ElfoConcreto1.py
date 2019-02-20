from PersonajesC.Personaje import Personaje
from PersonajesC import PersonajesSprites


class ElfoConcreto1(Personaje):

    def __init__(self):
        pass

    def SpritesAtacar(self):
        _SpritesAtaque = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/Elfo1/Ataque/Ataque' + str(i + 1) + '.png'
            _SpritesAtaque.append(PersonajesSprites.PersonajesSprites(imagen))
            return _SpritesAtaque

    def SpritesCaminar(self):
        _SpritesCaminar = []
        for i in range(0, 3):
            imagen = 'Imagenes/Elfos/Elfo1/Caminar/Caminar' + str(i + 1) + '.png'
            _SpritesCaminar.append(PersonajesSprites.PersonajesSprites(imagen))
            return _SpritesCaminar

    def SpritesMuerte(self):
        _SpritesMuerte = []
        for i in range(0, 5):
            imagen = 'Imagenes/Elfos/Elfo1/Muerte/Muerte' + str(i + 1) + '.png'
            _SpritesMuerte.append(PersonajesSprites.PersonajesSprites(imagen))
            return _SpritesMuerte
