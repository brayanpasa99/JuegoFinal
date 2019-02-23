from PersonajesC.Personaje import Personaje
from PersonajesC import PersonajesSprites


class OrcoConcreto3(Personaje):

    def __init__(self):
        pass

    def SpritesAtacar(self):
        _SpritesAtaque = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco3/Ataque/Ataque' + str(i + 1) + '.png'
            _SpritesAtaque.append(PersonajesSprites.PersonajesSprites(imagen))
            return _SpritesAtaque

    def SpritesCaminar(self):
        _SpritesCaminar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco3/Caminar/Caminar' + str(i + 1) + '.png'
            _SpritesCaminar.append(PersonajesSprites.PersonajesSprites(imagen))
            return _SpritesCaminar

    def SpritesMuerte(self):
        _SpritesMuerte = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco3/Muerte/Muerte' + str(i + 1) + '.png'

    def update(self):
        pass

    def dibujar(self):
        pass

