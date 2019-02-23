from PersonajesC.Personaje import Personaje
from PersonajesC import PersonajesSprites
import pygame
from pygame.locals import *
from random import randrange


class OrcoConcreto1(Personaje):

    def __init__(self):
        pass

    def SpritesAtacar(self):
        _SpritesAtaque = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco1/Ataque/Ataque' + str(i + 1) + '.png'
            _SpritesAtaque.append(PersonajesSprites.PersonajesSprites(imagen))
            return _SpritesAtaque

    def SpritesCaminar(self):
        _SpritesCaminar = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco1/Caminar/Caminar' + str(i + 1) + '.png'
            _SpritesCaminar.append(PersonajesSprites.PersonajesSprites(imagen))
            return _SpritesCaminar

    def SpritesMuerte(self):
        _SpritesMuerte = []
        for i in range(0, 7):
            imagen = 'Imagenes/Orcos/Orco1/Muerte/Muerte' + str(i + 1) + '.png'
            _SpritesMuerte.append(PersonajesSprites.PersonajesSprites(imagen))
            return _SpritesMuerte

    def update(self, ventana, imagen):

        teclas = pygame.key.get_pressed()

        if teclas[K_s]:
            pass

        self.dibujar(ventana, imagen)

    def dibujar(self, ventana, imagen):

        ventana.blit(imagen, (100, 100))



