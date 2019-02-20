from PersonajesC import OrcoSprites
import pygame

class OrcoConcreto1():

    def __init__(self):
        pass

    def SpritesAtacar(self):
        _SpritesAtaque = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco1/Ataque/Ataque'+str(i+1)+'.png'
            _SpritesAtaque.append(OrcoSprites.OrcosSprites(imagen))
            return _SpritesAtaque

    def SpritesCaminar(self):
        _SpritesCaminar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco1/Caminar/Caminar'+str(i+1)+'.png'
            _SpritesCaminar.append(OrcoSprites.OrcosSprites(imagen))
            return _SpritesCaminar

    def SpritesMuerte(self):
        _SpritesMuerte = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco1/Muerte/Muerte'+str(i+1)+'.png'
            _SpritesMuerte.append(OrcoSprites.OrcosSprites(imagen))
            return _SpritesMuerte

    def getSpritesAtacar(self):
        return OrcoConcreto1().SpritesAtacar()

    def getSpritesCaminar(self):
        return OrcoConcreto1().SpritesCaminar()

    def getSpritesMuerte(self):
        return OrcoConcreto1().SpritesMuerte()


